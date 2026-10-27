# AnnouncementArticleListRequest

Announcement article list query
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title_query** | **str** | Article title to use when querying announcements. | [optional] 
**page** | **str** | Page number. Optional. Pass as a string, for example \&quot;1\&quot;. | [optional] 
**size** | **str** | Number of articles to return per page. Optional. Pass as a string, for example \&quot;5\&quot;. | [optional] 
**tags** | **str** | Article tags | [optional] 
**timer** | **str** | Query announcements from the last N days, with N passed as a string. For example, on the 10th, pass \&quot;10\&quot; to query announcements from the 1st through the 10th. | [optional] 
**cate_name** | **str** | Announcement category name. | [optional] 
**cate_level** | **str** | Category level, passed as a string: \&quot;1\&quot; or \&quot;2\&quot;. | [optional] 
**sub_website_id** | **str** | Subsite ID, passed as a string: \&quot;0\&quot; for the main site or \&quot;177\&quot; for the Turkey site. Defaults to \&quot;0\&quot;. | [optional] [default to '0']
**pinned** | **int** | Whether to include pinned articles: 1 to include them or 0 to exclude them. Defaults to 1. | [optional] [default to 1]
**update_after** | **int** | Query announcement articles updated after this timestamp. | [optional] 
**lang** | **str** | Language code, for example \&quot;cn\&quot;. | [optional] 
**filter_empty_content** | **int** | Whether to exclude articles with empty content in the current language: 0 to keep them or 1 to exclude them. Defaults to 1. | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


