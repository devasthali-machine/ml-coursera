

setup VM
------------

```
gcloud beta compute --project=customer-support-610a3 instances create upd-machine --zone=us-west1-a --machine-type=n1-standard-1 --subnet=default --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=631068111578-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/cloud-platform --tags=http-server --image=debian-9-stretch-v20180510 --image-project=debian-cloud --boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=upd-machine

gcloud compute --project=customer-support-610a3 firewall-rules create default-allow-http --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=http-server
```

another example

```
gcloud beta compute --project=qwiklabs-gcp-45fa801c309cd3a1 instances create earthquake-lab-vm --zone=us-west1-a --machine-type=n1-standard-1 --subnet=default --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=979438154644-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/cloud-platform --tags=http-server,https-server --image=ubuntu-1804-bionic-v20180522 --image-project=ubuntu-os-cloud --boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=earthquake-lab

gcloud compute --project=qwiklabs-gcp-45fa801c309cd3a1 firewall-rules create default-allow-http --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=http-server

gcloud compute --project=qwiklabs-gcp-45fa801c309cd3a1 firewall-rules create default-allow-https --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:443 --source-ranges=0.0.0.0/0 --target-tags=https-server
```

```
gcloud auth login

gcloud compute zones list
NAME                       REGION                   STATUS  NEXT_MAINTENANCE  TURNDOWN_DATE
us-east1-b                 us-east1                 UP
us-east1-c                 us-east1                 UP
us-east1-d                 us-east1                 UP
us-east4-c                 us-east4                 UP
us-east4-b                 us-east4                 UP
us-east4-a                 us-east4                 UP
us-central1-c              us-central1              UP
us-central1-a              us-central1              UP
us-central1-f              us-central1              UP
us-central1-b              us-central1              UP
asia-northeast1-c          asia-northeast1          UP
us-west1-b                 us-west1                 UP
us-west1-c                 us-west1                 UP
us-west1-a                 us-west1                 UP
europe-west4-a             europe-west4             UP
europe-west4-b             europe-west4             UP
europe-west4-c             europe-west4             UP
europe-west1-b             europe-west1             UP
europe-west1-d             europe-west1             UP
europe-west1-c             europe-west1             UP
europe-west3-b             europe-west3             UP
europe-west3-c             europe-west3             UP
europe-west3-a             europe-west3             UP
europe-west2-c             europe-west2             UP
europe-west2-b             europe-west2             UP
europe-west2-a             europe-west2             UP
asia-east1-b               asia-east1               UP
asia-east1-a               asia-east1               UP
asia-east1-c               asia-east1               UP
asia-southeast1-b          asia-southeast1          UP
asia-southeast1-a          asia-southeast1          UP
asia-southeast1-c          asia-southeast1          UP
asia-northeast1-b          asia-northeast1          UP
asia-northeast1-c          asia-northeast1          UP
asia-northeast1-a          asia-northeast1          UP
asia-south1-c              asia-south1              UP
asia-south1-b              asia-south1              UP
asia-south1-a              asia-south1              UP
australia-southeast1-b     australia-southeast1     UP
australia-southeast1-c     australia-southeast1     UP
australia-southeast1-a     australia-southeast1     UP
southamerica-east1-b       southamerica-east1       UP
southamerica-east1-c       southamerica-east1       UP
southamerica-east1-a       southamerica-east1       UP
northamerica-northeast1-a  northamerica-northeast1  UP
northamerica-northeast1-b  northamerica-northeast1  UP
northamerica-northeast1-c  northamerica-northeast1  UP

sudo apt-get update && sudo apt-get --only-upgrade install kubectl google-cloud-sdk google-cloud-sdk-app-engine-grpc google-cloud-sdk-pubsub-emulator google-cloud-sdk-app-eng ine-go google-cloud-sdk-datastore-emulator google-cloud-sdk-app-engine-python google-cloud-sdk-cbt google-cloud-sdk-bigtable-emulator google-cloud-sdk-app-engine-python-extra s google-cloud-sdk-datalab google-cloud-sdk-app-engine-java

sudo apt-get install google-cloud-sdk-datalab
```

training
----------

```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
cd training-data-analyst/courses/machine_learning/deepdive/01_googleml/earthquakes
bash ingest.sh
```

```
head earthquakes.csv
time,latitude,longitude,depth,mag,magType,nst,gap,dmin,rms,net,id,updated,place,type,horizontalError,depthError,magError,magNst,status,locationSource,magSource
2018-05-30T03:33:04.030Z,19.4046669,-155.3063354,2.07,2.36,ml,11,154,0.02147,0.29,hv,hv70207327,2018-05-30T03:38:54.290Z,"7km WSW of Volcano, Hawaii",earthquake,0.85,1.02,0.38,8,automatic,hv,hv
```

```
bash install-missing.sh
python transform.py

ll
total 872
drwxrwxr-x 3 google484640_student google484640_student   4096 May 30 03:56 ./
drwxrwxr-x 8 google484640_student google484640_student   4096 May 30 03:51 ../
-rw-rw-r-- 1 google484640_student google484640_student    637 May 30 03:51 commands.sh
-rw-rw-r-- 1 google484640_student google484640_student 534991 May 30 03:48 earthquakes.csv
-rw-rw-r-- 1 google484640_student google484640_student    751 May 30 03:51 earthquakes.htm
-rw-rw-r-- 1 google484640_student google484640_student 319434 May 30 03:56 earthquakes.png
-rwxrwxr-x 1 google484640_student google484640_student    759 May 30 03:51 ingest.sh*
-rwxrwxr-x 1 google484640_student google484640_student    680 May 30 03:51 install_missing.sh*
drwxrwxr-x 2 google484640_student google484640_student   4096 May 30 03:51 scheduled/
-rwxrwxr-x 1 google484640_student google484640_student   3074 May 30 03:51 transform.py*
```

- create a storage-bucket `earthquake-lab-storage`

```
gsutil cp earthquakes.* gs://earthquake-lab-storage/earthquakes
```

- share the storage files publicly
- access https://storage.googleapis.com/earthquake-lab-storage/earthquakes/earthquakes.htm

- enable `Cloud Source Repositories API`

create another datalab VM
-----------------

```
datalab create earthquake-lab-vm --zone us-west1-a
Creating the repository datalab-notebooks
Creating the instance earthquake-lab
Created [https://www.googleapis.com/compute/v1/projects/customer-support-610a3/zones/us-west1-a/instances/earthquake-lab].
Connecting to earthquake-lab.
This will create an SSH tunnel and may prompt you to create an rsa key pair. To manage these keys, see https://cloud.google.com/compute/docs/instanc
es/adding-removing-ssh-keys
Waiting for Datalab to be reachable at http://localhost:8081/
Generating public/private rsa key pair.
```
