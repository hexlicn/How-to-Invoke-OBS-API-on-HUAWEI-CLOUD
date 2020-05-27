# Huawei-Cloud-OBS-API-demo
How to invoke Huawei Cloud OBS API by postman/curl

Steps:
1. Please run hwc-obs-API-sig.py to get signature, sample output

Wed, 27 May 2020 16:16:07 GMT
PUT

application/xml
Wed, 27 May 2020 16:16:07 GMT
/test-l00490846/
Kpqb6GtAJb6ibHCm514Mom5BOOU=

2. Input Postman header as following: 
curl --location --request PUT 'https://test-l00490846.obs.af-south-1.myhuaweicloud.com' \
--header 'Content-Type: application/xml' \
--header 'CanonicalizedResource: /test-l00490846/' \
--header 'Authorization: OBS AQJ7KZJR00DDWVOSEWIP:Kpqb6GtAJb6ibHCm514Mom5BOOU=' \
--header 'Date: Wed, 27 May 2020 16:16:07 GMT' \
--data-raw '<CreateBucketConfiguration xmlns="http://obs.cn-north-4.myhuaweicloud.com/doc/2015-06-30/"> 
    <Location>af-south-1</Location> 
</CreateBucketConfiguration> '

NOTES: "Authorization" format should be OBS <your_ak>:<your_signature_from_step_1>
       "Date" format should be the same output with step 1
       Interval <= 15mins, Please update your 'sk' on the Python script accordingly

More details, please refer to https://support.huaweicloud.com/intl/en-us/api-obs/en-us_topic_0031051947.html
