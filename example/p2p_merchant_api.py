#!/usr/bin/env python
# coding: utf-8

import logging

from gate_api import (
    ApiClient, Configuration, P2pApi,
    AdsDetailRequest, AdsListRequest, AdsUpdateStatus,
    CancelOrder, ConfirmPayment, ConfirmReceipt,
    GetChatsListRequest, GetCompletedTransactionListRequest,
    GetCounterpartyUserInfoRequest, GetMyselfPaymentRequest,
    GetPendingTransactionListRequest, GetTransactionDetailsRequest,
    MyAdsListRequest, PlaceBizPushOrder,
    SendChatMessageRequest, UploadChatFile,
)
from gate_api.exceptions import ApiException

from config import RunConfig

logger = logging.getLogger(__name__)


def p2p_merchant_demo(run_config):
    # type: (RunConfig) -> None
    """
    P2P Merchant API demo. Covers all endpoints in p2p-merchant-api.yaml in business order:
    Account -> Ads -> Orders (list & detail) -> Order actions -> Chat.
    """
    config = Configuration(
        key=run_config.api_key,
        secret=run_config.api_secret,
        host=run_config.host_used,
    )
    api = P2pApi(ApiClient(config))

    try:
        # ============================================================
        # 1. Account - user info and payment methods
        # ============================================================
        logger.info("=== 1. P2P Merchant Account ===")

        user_info = api.p2p_merchant_account_get_user_info()
        logger.info("User info: %s", user_info)

        myself_payment = api.p2p_merchant_account_get_myself_payment(
            get_myself_payment_request=GetMyselfPaymentRequest(fiat="USD")
        )
        logger.info("Payment methods: %s", myself_payment)

        # ============================================================
        # 2. Ads - my ads, market ads, ad detail; place/update (write ops commented)
        # ============================================================
        logger.info("=== 2. P2P Ads ===")

        my_ads = api.p2p_merchant_books_my_ads_list(
            my_ads_list_request=MyAdsListRequest(asset="USDT", fiat_unit="USD", trade_type="sell")
        )
        logger.info("My ads list: %s", my_ads)

        ads = api.p2p_merchant_books_ads_list(
            AdsListRequest(asset="USDT", fiat_unit="USD", trade_type="sell")
        )
        logger.info("Market ads list: %s", ads)

        if my_ads and getattr(my_ads, "data", None) and getattr(my_ads.data, "lists", None) and my_ads.data.lists:
            first_ad_id = getattr(my_ads.data.lists[0], "id", None) or getattr(my_ads.data.lists[0], "orderid", None)
            if first_ad_id is not None:
                ad_detail = api.p2p_merchant_books_ads_detail(
                    AdsDetailRequest(adv_no=str(first_ad_id))
                )
                logger.info("Ad detail: %s", ad_detail)
        # Example when no my ads (replace with real adv_no):
        # ad_detail = api.p2p_merchant_books_ads_detail(
        #     AdsDetailRequest(adv_no="2124287072")
        # )

        # Place/edit ad (write op, use with care)
        # api.p2p_merchant_books_place_biz_push_order(
        #     PlaceBizPushOrder(
        #         currency_type="USDT",
        #         exchange_type="USD",
        #         type="0",
        #         unit_price="7.20",
        #         number="1000",
        #         min_amount="100",
        #         max_amount="1000",
        #         pay_type="bank",
        #         rate_fixed="1",
        #         hide_payment="0",
        #         expire_min="15",
        #         trade_tips="Please pay within 15 minutes",
        #         auto_reply="Auto reply example",
        #     )
        # )

        # Update ad status: 1=active, 3=inactive, 4=closed
        # api.p2p_merchant_books_ads_update_status(
        #     AdsUpdateStatus(adv_no=123456, adv_status=1)
        # )

        # ============================================================
        # 3. Orders - pending list, completed list, order detail
        # ============================================================
        logger.info("=== 3. P2P Orders ===")

        pending_list = api.p2p_merchant_transaction_get_pending_transaction_list(
            GetPendingTransactionListRequest(
                crypto_currency="USDT",
                fiat_currency="USD",
                order_tab="pending",
                select_type="sell",
                # status="OPEN",
                # txid=40036321,
                # start_time=1700000000,
                # end_time=1700086399,
            )
        )
        logger.info("Pending orders: %s", pending_list)

        completed_list = api.p2p_merchant_transaction_get_completed_transaction_list(
            GetCompletedTransactionListRequest(
                crypto_currency="USDT",
                fiat_currency="USD",
                # select_type="sell",
                # status="ACCEPT",
                # txid=40036321,
                # start_time=1700000000,
                # end_time=1700086399,
                # query_dispute=0,
                # page=1,
                # per_page=20,
            )
        )
        logger.info("Completed orders: %s", completed_list)

        txid_for_detail = None
        for resp in (pending_list, completed_list):
            if not resp or not getattr(resp, "data", None):
                continue
            data = resp.data
            lst = getattr(data, "list", None) or getattr(data, "lists", None)
            if lst and len(lst) > 0:
                first = lst[0]
                txid_for_detail = getattr(first, "txid", None)
                if txid_for_detail is not None:
                    break
        if txid_for_detail is not None:
            order_detail = api.p2p_merchant_transaction_get_transaction_details(
                GetTransactionDetailsRequest(
                    txid=txid_for_detail,
                    # channel="web3",
                )
            )
            logger.info("Order detail: %s", order_detail)
            if order_detail and getattr(order_detail, "data", None):
                biz_uid = getattr(order_detail.data, "its_uid", None)
                if biz_uid:
                    counterparty = api.p2p_merchant_account_get_counterparty_user_info(
                        GetCounterpartyUserInfoRequest(biz_uid=biz_uid)
                    )
                    logger.info("Counterparty info: %s", counterparty)
            chats = api.p2p_merchant_chat_get_chats_list(
                GetChatsListRequest(
                    txid=txid_for_detail,
                    # lastreceived=1700000000,
                    # firstreceived=1700000000,
                )
            )
            logger.info("Chat list: %s", chats)
        # Example when no orders (replace with real txid):
        # order_detail = api.p2p_merchant_transaction_get_transaction_details(
        #     GetTransactionDetailsRequest(txid=40036321)
        # )
        # chats = api.p2p_merchant_chat_get_chats_list(
        #     GetChatsListRequest(txid=40036321)
        # )

        # ============================================================
        # 4. Order actions - confirm payment, confirm receipt, cancel (write ops, commented)
        # ============================================================
        logger.info("=== 4. P2P Order actions (examples commented) ===")

        # Buyer confirms payment
        # api.p2p_merchant_transaction_confirm_payment(
        #     ConfirmPayment(trade_id="40036321", payment_method="bank")
        # )

        # Seller confirms receipt and release
        # api.p2p_merchant_transaction_confirm_receipt(
        #     ConfirmReceipt(trade_id="40036321")
        # )

        # Cancel order
        # api.p2p_merchant_transaction_cancel(
        #     CancelOrder(
        #         trade_id="40036321",
        #         reason_id="1",
        #         reason_memo="I don't want to trade anymore.",
        #     )
        # )

        # ============================================================
        # 5. Chat - send message, upload file (write ops, commented)
        # ============================================================
        logger.info("=== 5. P2P Chat write ops (examples commented) ===")

        # Send text message (requires real txid)
        # api.p2p_merchant_chat_send_chat_message(
        #     SendChatMessageRequest(
        #         txid=40036321,
        #         message="Please complete the payment within 15 minutes.",
        #         type=0,
        #     )
        # )

        # Upload chat file (image/video base64)
        # api.p2p_merchant_chat_upload_chat_file(
        #     UploadChatFile(
        #         image_content_type="image/png",
        #         base64_img="BASE64_STRING",
        #     )
        # )

        logger.info("=== P2P Merchant demo finished ===")

    except ApiException as e:
        logger.error("Gate API exception: %s", e)
    except Exception as e:
        logger.exception("Unexpected exception: %s", e)
