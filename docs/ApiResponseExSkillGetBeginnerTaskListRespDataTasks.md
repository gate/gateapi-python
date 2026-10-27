# ApiResponseExSkillGetBeginnerTaskListRespDataTasks

Getting started mission information. `task_center_id` and `status` are included in required: both are allowed to be 0 (registration tasks, download tasks to be received), And avoid Go SDK using omitempty for integer zero values, which will cause fields to be lost during client serialization.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**welfare_task_id** | **int** | Rewards Center task ID | [optional] 
**task_center_id** | **int** | Task center task ID (fixed at 0 for registration tasks) | 
**task_type** | **int** | Task type: 1&#x3D;KYC secondary certification 2&#x3D;Spot 3&#x3D;Contract 4&#x3D;Invitation 5&#x3D;Quantification 6&#x3D;Yu Bibao 7&#x3D;startup 8&#x3D;First deposit 10&#x3D;Registration task 11&#x3D;Guide task 23&#x3D;Download task | [optional] 
**task_name** | **str** | Task name | [optional] 
**task_desc** | **str** | Task description, may contain &lt;span&gt; highlight tags | [optional] 
**reward_num** | **str** | Reward value | [optional] 
**reward_unit** | **str** | Reward unit (e.g., USDT, BTC) | [optional] 
**prize_type** | **int** | Reward type: 1 &#x3D; points, 2 &#x3D; regular coupon, 3 &#x3D; VIP coupon | [optional] 
**status** | **int** | Task status: 0&#x3D;Not claimed (typically a download task waiting to be claimed) 1&#x3D;Received/in progress 2&#x3D;Completed and waiting to be claimed 3&#x3D;Rewards in progress 4&#x3D;Completed/settled 5&#x3D;Expired | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


