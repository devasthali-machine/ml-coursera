

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

enable `Cloud Source Repositories API`

```
datalab create earthquake-lab --zone us-west1-a
Creating the repository datalab-notebooks
Creating the instance earthquake-lab
Created [https://www.googleapis.com/compute/v1/projects/customer-support-610a3/zones/us-west1-a/instances/earthquake-lab].
Connecting to earthquake-lab.
This will create an SSH tunnel and may prompt you to create an rsa key pair. To manage these keys, see https://cloud.google.com/compute/docs/instanc
es/adding-removing-ssh-keys
Waiting for Datalab to be reachable at http://localhost:8081/
Generating public/private rsa key pair.
```
