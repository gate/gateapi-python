# AccountKeyInfo

Main Account API Key Information
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **int** | API key status: 1 - Normal, 2 - Locked, 3 - Frozen (can only be modified, default is 1 when creating)API Key Status: 1 - Normal, 2 - Locked, 3 - Frozen (can only be modified; default is 1 upon creation) | [optional] 
**mode** | **int** | User mode: 1 - Classic mode, 2 - Legacy unified mode (can only be specified when creating, cannot be modified) | [optional] 
**name** | **list[str]** | API Key Remark | [optional] 
**currency_pairs** | **list[str]** | Trading Pair Whitelist, Maximum 30 Pairs | [optional] 
**user_id** | **int** | User ID | [optional] 
**ip_whitelist** | **list[str]** | IP Whitelist | [optional] 
**perms** | [**list[AccountKeyInfoPerms]**](AccountKeyInfoPerms.md) |  | [optional] 
**key** | [**AccountDetailKey**](AccountDetailKey.md) |  | [optional] 
**created_at** | **str** | Created time | [optional] [readonly] 
**updated_at** | **str** | Last Update Time | [optional] [readonly] 
**last_access** | **str** | Last Access Time | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


