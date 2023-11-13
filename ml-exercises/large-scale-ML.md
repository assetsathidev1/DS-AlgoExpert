# Large Scale ML Notes

## Introduction
- Topics to be covered: Data Ingestion, Exploration, Experiementation(MAB, AB etc), Training, Serving, Monitoring, Debugging, and Scaling.

## Data Ingestions
- Broadly large scale applications can be classified into two categories: Batch and Streaming.
- For streaming applications, we can use Kafka, Kinesis, PubSub etc.
- For batch applications, we can use Airflow, Luigi, Oozie etc.
- The overal structure remains same: Producer -> Queue/Broker -> Consumer/Storage.
- Streaming Ingestion
    - Examples of producers for streaming could be: Click streams from apps, CDC from DBs, Logs from servers, Live video feeds etc.
    - Examples of brokers for streaming could be: Kafka, Kinesis, PubSub etc.
    - Examples of consumers for streaming could be: Spark Streaming, Flink, Storm etc.
- Batch Ingention
    - Examples of producers for batch could be: Data dumps from (OLTP) DBs like MySQLdump, Postgres etc.
    - Examples of brokers for batch too are kafka, pubsub, kinesis etc
    - Examples of consumers for batch could be: Spark, Hive, HDFS etc.
- The way to ensure `exactly once semantics` b/w producer and broker: is to use a unique id for each message and use that to dedupe messages.; My inference is that, the unique id is created per msg per producer. example: `Kafka Transactions / Kafka Streams API`
- The way to ensure `exactly once semantics` b/w broker and consumer: is to use a similar solution like `HDFS Sink` etc.
- `OLTP` stands for Online Transaction Processing. It is a class of software applications capable of supporting transaction-oriented programs. OLTP systems are designed to process small, relatively simple transactions that are generally executed frequently as well as concurrently.
- Example: A DB that maintains the number of subscribers to a particual service
- `OLAP` stands for Online Analytical Processing. It is a class of software programs capable of supporting complex analytical programs. OLAP systems are designed to analyze large volumes of data.
- Example: A hadoop cluster that maintins the user subscription history; when did they subscribe, when did they unsubscribe etc. Basis that we can look at how the usage of the service has changed over time and may be come up with hypothesis on why it has changed.
- Live video stream can be enabled using `HLS` (Http Live Streaming) or `DASH` (Dynamic Adaptive Streaming over HTTP). The way it works is that the video is broken down into small chunks and each chunk is encoded at different bitrates. The client can then choose the bitrate based on the network conditions. The client can also switch between bitrates during the playback. The client can also choose to download the chunks in advance to avoid buffering.
- The systems looks something like this: Producer(Video MP4 etc) -> Encoder(HLS etc) -> CDN(broker/queue) -> Client(browser,app etc). The CDN is responsible for caching the chunks and serving them to the client. The client can be a browser or a mobile app.

### Kafka
- Kafka is a distributed streaming platform. It is a distributed commit log.
- `Kafka` has `brokers` that can host multiple `topics`. 
    - Each `topic` can have multiple `partitions`. 
    - Each `partition` can have multiple `replicas`. 
    - Each `replica` is a `leader` or a `follower`. 
    - The `leader` is responsible for handling read and write requests. 
    - The `follower` is responsible for replicating the data from the `leader`. 
    - The `leader` and `follower` can be on the same `broker` or different `brokers`.
- `Zookeeper` is used for leader election in a `broker` , maintaining the metadata and handles the failover.
- `Broker Cluster` can be configured to handle large volumes/scale of data inflow.
- This is how kafka gives us a scalability and fault tolerance.
- `Kinises`: Imagine Kafka, but with `Shards` instead of `Brokers`

- General Considerations for ingestion:
    - Size of individual data (bytes, KB, MB, GB per msg)
    - Rate of data ingestion (per second, per minute etc)
    - Data types supported and changes in them how can it be handled
    - High Availability(different availability zones) and how fault tolerant  

### HDFS (Hadoop Distributed File System)
- There are `Data Nodes` and a `Name node`; `Name node` tells the `HDFS client` which `Data Node` to read/write from/to.
- `Data Nodes` are responsible for storing the data and `Name Node` is responsible for storing the metadata.
- `Name node` does a `heartbeat` check with the `Data Nodes` to ensure they are up and running.
- There is a default replication factor of 3. So, each block(a part of data) is replicated 3 times mostly across different data nodes.
- There is also a `Passive Name node` that is kept in sync with the `Active Name node` using `Journal Nodes`. So incase the `Active name node` goes down the passive can come up.
- `Journal Nodes` are responsible for storing the edits to the `Name Node` and are used to keep the `Active Name Node` and `Passive Name Node` in sync.
- A Zookeeper cluster is used to elect the `Active Name Node` and `Passive Name Node`; by heartbeat checks.
- HDFS can scale to save 10s of Petabytes of data
- Hadoop 3 uses `Erasure Coding` instead of `Replication` to save space. It is a way to encode the data in such a way that it can be recovered even if some of the data is lost. It is similar to RAID 5.

### Storage Formats:
- `Avro` is a row based binary format that is used to store data in a compact way. It is used for data serialization. 
    - Row based, good for queries that require all columns
    - Good for write heavy workloads
    - Supports JSON schema so easy to handle changes in schema

- `Parquet` is a columnar storage format. Has better compression and is used for analytics. Example: imagine a city column in a usecase, there might be a lot of users from few unique cities, so this can be stored in a compact way.  
    - Good for Sparse data
    - Good for read heavy workloads
    - Good for queries that require only few columns


## Data Processing
- Simplified Requirements would be:
    - Cluster resource mgmt (CPU, RAM left etc)
    - Computational dependency mgmt (in what order does the jobs/tasks need to run)
    - Saving final result back to HDFS
    - Bonus: Share the same HDFS cluster where the data resides so we can avoid network transfer
- Solution: Apache Spark and Apache Yarn

### Apache Yarn
- Yarn (Yet another resource negotiator) has a few components: 
- `ResourceManager` is responsible for managing the resources in the cluster. 
    - `Scheduler` allocates cluster resources to `NodeManagers`. 
    - `ApplicationManager` that is responsible for managing the lifecycle of the applications.
- `Node Manager` is responsible for managing the resources on a single node. 
    - `Container` is a resource allocation on a single node where the actual code is run
    - Once the code run is completed the `Container` is released and the resources are freed up and this info is updated to the `ResourceManager`.
    - Negotiates with the `ResourceManager` to get the resources for the `Container`.
    - Reports resource usage back to the `ResourceManager`.
- `Application Master` request for more containers or more resources with the `ResourceManager`
- Effectively YARN abstracts the distributed resources in the cluster and makes it look like a single giant machine. 
- This solves the cluster mgmt problem. But does not tackle the computational dependency mgmt problem.

### Apache Spark
- Spark has a few components:
- `Driver` is responsible for managing the lifecycle of the application. 
    - It is responsible for creating the `SparkContext` and `SparkSession`. 
    - It is responsible for creating the `DAG` and submitting it to the `Cluster Manager`. 
    - It is responsible for monitoring the `DAG` and reporting the status back to the user.
    - Also Validates the data, Optimises the code and creates an `RDD DAG`  (Resilenet Distributed dataset(unit of data) - directed acyclic graph)
- `Cluster Manager` is responsible for managing the resources in the cluster. YARN is used for this. 
- `Executor` is responsible for running the tasks. 
    - It is responsible for running the `Task` and reporting the status back to the `Driver`. 
    - It is responsible for caching the data in memory and disk. 
    - It is responsible for reading and writing the data from and to the `HDFS`. 
- This can help in optimally using the resources in parallel and also solve our computational dependency mgmt problem. And since this can be installed on `HDFS` cluster we can avoid network transfer.

- How does Spark fit with Yarn:
    - The `Driver` is `Application Manager`
    - The `Executors` are `Containers` on `Node Managers`
- A single point of failure in this setup could be the `Resource Manager` and that can be solved by  `Zookeeper` by having a passive stand by `Resource Manager` and using `Zookeeper` to elect the `Active Resource Manager`.
- `Data processing Orchestration` is the process of managing the data processing pipeline. It is responsible for managing the dependencies, scheduling the jobs, monitoring the jobs, retrying the jobs, alerting the users etc.
- `Apache Airflow` is and example software to handle this orchestration. 
### Apache Airflow
- Contains a `Web Server` and a `Scheduler`.
- `Web Server` is a flask app for showing each `DAG` and the status of each `Task` in the `DAG` and the history of the same.
- `Scheduler`(`rabbitmq`) is responsibile for:
    - monitoring task `run status`
    - fetch `DAGs` from `DAG store`(usually a `s3` or a file store)
    - sends `DAGs` to execution queue
    - writes `DAG` run status to db(`postgres`) for history
- `Worker`(`celery`) is responsible for:
    - fetching `DAG` from execution queue
    - executing `DAG` tasks
    - writing `DAG` run status to db for history
- This way we can handle 1000s of jobs in a scheduled automated manner.