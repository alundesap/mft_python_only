# mft_python_only

# Determine which version of Python is available by running this in a Unix shell
```
ver=$(cf buildpacks | grep python | cut -d '-' -f 4 | cut -d '.' -f 1-3) ; echo ; echo "Browse to this page for python versions available in this buildpack." ; echo ; echo "https://github.com/cloudfoundry/python-buildpack/releases/tag/$ver" ; echo
```

# Deploy by using the "cf push" command with this as the current directory.

```
cf push
```

Output:
```
App Bindetermination_10_01_2020 was started using this command `python3 server.py`

Showing health and status for app Bindetermination_10_01_2020 in org ConcileTime / space dev as andrew.lunde@sap.com...
OK

requested state: started
instances: 1/1
usage: 512M x 1 instances
urls: bindetermination-10-01-2020.cfapps.us10.hana.ondemand.com
last uploaded: Tue Jan 14 20:25:07 UTC 2020
stack: cflinuxfs3
buildpack: python_buildpack

     state     since                    cpu    memory          disk           details
#0   running   2020-01-14 03:26:22 PM   0.0%   37.5M of 512M   386.8M of 1G
```

https://bindetermination-10-01-2020.cfapps.us10.hana.ondemand.com/env

Output:
```
Key Environment variables... 
PORT: 8080
PYTHONHOME: /home/vcap/deps/0/python
PYTHONPATH: /home/vcap/deps/0
VCAP_APPLICATION: {
    "application_id": "a72c0856-c85c-4940-bf06-226c9b715739",
    "application_name": "Bindetermination_10_01_2020",
    "application_uris": [
        "bindetermination-10-01-2020.cfapps.us10.hana.ondemand.com"
    ],
    "application_version": "cea67ee5-427d-41c4-810f-64a441c3da09",
    "cf_api": "https://api.cf.us10.hana.ondemand.com",
    "host": "0.0.0.0",
    "instance_id": "e4ab7063-7cd2-4890-4089-6e33",
    "instance_index": 0,
    "limits": {
        "disk": 1024,
        "fds": 16384,
        "mem": 512
    },
    "name": "Bindetermination_10_01_2020",
    "organization_id": "4d641712-8d17-45c6-adca-65c4f61e4202",
    "organization_name": "ConcileTime",
    "port": 8080,
    "process_id": "a72c0856-c85c-4940-bf06-226c9b715739",
    "process_type": "web",
    "space_id": "9145fa0f-0a3b-4252-bffb-87bd02288e9b",
    "space_name": "dev",
    "uris": [
        "bindetermination-10-01-2020.cfapps.us10.hana.ondemand.com"
    ],
    "version": "cea67ee5-427d-41c4-810f-64a441c3da09"
}
VCAP_SERVICES: {}
```

# Now bind a service instance to the app and restage it.

```
cf bind-service Bindetermination_10_01_2020 CONCILE_COM
cf restage Bindetermination_10_01_2020
```

Output:
```
Key Environment variables... 
PORT: 8080
PYTHONHOME: /home/vcap/deps/0/python
PYTHONPATH: /home/vcap/deps/0
VCAP_APPLICATION: {
    "application_id": "a72c0856-c85c-4940-bf06-226c9b715739",
    "application_name": "Bindetermination_10_01_2020",
    "application_uris": [
        "bindetermination-10-01-2020.cfapps.us10.hana.ondemand.com"
    ],
    "application_version": "1aabfa17-b6ad-43c8-8610-8528a772bd3a",
    "cf_api": "https://api.cf.us10.hana.ondemand.com",
    "host": "0.0.0.0",
    "instance_id": "f7dd86b2-d32a-41bc-55c7-5bb2",
    "instance_index": 0,
    "limits": {
        "disk": 1024,
        "fds": 16384,
        "mem": 512
    },
    "name": "Bindetermination_10_01_2020",
    "organization_id": "4d641712-8d17-45c6-adca-65c4f61e4202",
    "organization_name": "ConcileTime",
    "port": 8080,
    "process_id": "a72c0856-c85c-4940-bf06-226c9b715739",
    "process_type": "web",
    "space_id": "9145fa0f-0a3b-4252-bffb-87bd02288e9b",
    "space_name": "dev",
    "uris": [
        "bindetermination-10-01-2020.cfapps.us10.hana.ondemand.com"
    ],
    "version": "1aabfa17-b6ad-43c8-8610-8528a772bd3a"
}
VCAP_SERVICES: {
    "hana": [
        {
            "binding_name": null,
            "credentials": {
                "certificate": "-----BEGIN CERTIFICATE-----\nMIIDrzCCApegAwIBAgIQCDvgVpBCRrGhdWrJWZHHSjANBgkqhkiG9w0BAQUFADBh\nMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\nd3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBD\nQTAeFw0wNjExMTAwMDAwMDBaFw0zMTExMTAwMDAwMDBaMGExCzAJBgNVBAYTAlVT\nMRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxGTAXBgNVBAsTEHd3dy5kaWdpY2VydC5j\nb20xIDAeBgNVBAMTF0RpZ2lDZXJ0IEdsb2JhbCBSb290IENBMIIBIjANBgkqhkiG\n9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4jvhEXLeqKTTo1eqUKKPC3eQyaKl7hLOllsB\nCSDMAZOnTjC3U/dDxGkAV53ijSLdhwZAAIEJzs4bg7/fzTtxRuLWZscFs3YnFo97\nnh6Vfe63SKMI2tavegw5BmV/Sl0fvBf4q77uKNd0f3p4mVmFaG5cIzJLv07A6Fpt\n43C/dxC//AH2hdmoRBBYMql1GNXRor5H4idq9Joz+EkIYIvUX7Q6hL+hqkpMfT7P\nT19sdl6gSzeRntwi5m3OFBqOasv+zbMUZBfHWymeMr/y7vrTC0LUq7dBMtoM1O/4\ngdW7jVg/tRvoSSiicNoxBN33shbyTApOB6jtSj1etX+jkMOvJwIDAQABo2MwYTAO\nBgNVHQ8BAf8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUA95QNVbR\nTLtm8KPiGxvDl7I90VUwHwYDVR0jBBgwFoAUA95QNVbRTLtm8KPiGxvDl7I90VUw\nDQYJKoZIhvcNAQEFBQADggEBAMucN6pIExIK+t1EnE9SsPTfrgT1eXkIoyQY/Esr\nhMAtudXH/vTBH1jLuG2cenTnmCmrEbXjcKChzUyImZOMkXDiqw8cvpOp/2PV5Adg\n06O/nVsJ8dWO41P0jmP6P6fbtGbfYmbW0W5BjfIttep3Sp+dWOIrWcBAI+0tKIJF\nPnlUkiaY4IBIqDfv8NZ5YBberOgOzW6sRBc4L0na4UU+Krk2U886UAb3LujEV0ls\nYSEY1QSteDwsOoBrp+uvFRTp2InBuThs4pFsiv9kuXclVzDAGySj4dzp30d8tbQk\nCAUw7C29C79Fv1C5qfPrmAESrciIxpg0X40KPMbp1ZWVbd4=\n-----END CERTIFICATE-----\n",
                "driver": "com.sap.db.jdbc.Driver",
                "hdi_password": "Be5Pbh-yAciQGCKO.-rJ-WSUYByIeBeXx.vzD.H19gXhrYYvnVxmgKWruA6Y5THEpHmZ.GYZiLolw07y0P-42GoIapQedXVT.ykyILzE.zsfEyxAbOIlATANHbf89t-o",
                "hdi_user": "CONCILE_COM_V0_DEV_AWBCSAK5VZTQ7Y481P3RW5SKJ_DT",
                "host": "zeus.hana.prod.us-east-1.whitney.dbaas.ondemand.com",
                "password": "Rm1Zt84tnC1egEFbpwdmdP47FP_1GbcwTDE5qe3AmZ9UAEYRkEbwi3wO402s29j_iI0MKnFcuvutIUZOF.Gw4Q0Lp-TiVmXsBeP-5qXXLnIli0R8NolfhIyKUZa92xwh",
                "port": "20217",
                "schema": "CONCILE_COM_V0_DEV",
                "url": "jdbc:sap://zeus.hana.prod.us-east-1.whitney.dbaas.ondemand.com:20217?encrypt=true&validateCertificate=true&currentschema=CONCILE_COM_V0_DEV",
                "user": "CONCILE_COM_V0_DEV_AWBCSAK5VZTQ7Y481P3RW5SKJ_RT"
            },
            "instance_name": "CONCILE_COM",
            "label": "hana",
            "name": "CONCILE_COM",
            "plan": "hdi-shared",
            "provider": null,
            "syslog_drain_url": null,
            "tags": [
                "hana",
                "database",
                "relational"
            ],
            "volume_mounts": []
        }
    ]
}
host: zeus.hana.prod.us-east-1.whitney.dbaas.ondemand.com
port: 20217
user: CONCILE_COM_V0_DEV_AWBCSAK5VZTQ7Y481P3RW5SKJ_RT
pass: Rm1Zt84tnC1egEFbpwdmdP47FP_1GbcwTDE5qe3AmZ9UAEYRkEbwi3wO402s29j_iI0MKnFcuvutIUZOF.Gw4Q0Lp-TiVmXsBeP-5qXXLnIli0R8NolfhIyKUZa92xwh
```
