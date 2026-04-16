# ApiResponseExSkillGetBeginnerTaskListRespDataTasks

入门任务信息。`task_center_id` 与 `status` 列入 required：二者均允许为 0（注册任务、待领取下载任务）， 且避免 Go SDK 对整型零值使用 omitempty 导致客户端序列化时丢失字段。
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**welfare_task_id** | **int** | Rewards Center task ID | [optional] 
**task_center_id** | **int** | Task center task ID (fixed at 0 for registration tasks) | 
**task_type** | **int** | 任务类型：1&#x3D;KYC二级认证 2&#x3D;现货 3&#x3D;合约 4&#x3D;邀请 5&#x3D;量化 6&#x3D;余币宝 7&#x3D;startup 8&#x3D;首次入金 10&#x3D;注册任务 11&#x3D;引导任务 23&#x3D;下载任务 | [optional] 
**task_name** | **str** | Task name | [optional] 
**task_desc** | **str** | Task description, may contain &lt;span&gt; highlight tags | [optional] 
**reward_num** | **str** | Reward value | [optional] 
**reward_unit** | **str** | Reward unit (e.g., USDT, BTC) | [optional] 
**prize_type** | **int** | Reward type: 1 &#x3D; points, 2 &#x3D; regular coupon, 3 &#x3D; VIP coupon | [optional] 
**status** | **int** | 任务状态：0&#x3D;未领取（典型为待领取下载任务） 1&#x3D;已领取/进行中 2&#x3D;已完成待领奖 3&#x3D;发奖中 4&#x3D;已完成/已结算 5&#x3D;已过期 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


