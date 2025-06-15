## Taxi Information and Monitoring Engine (TIME)

Welcome to the TIME Dashboard! This project provides real-time monitoring and analysis of a fleet of 10,000+ taxis, displaying and updating live data including average speed, current speed, location, and timestamps. As the dashboard is fed live data, the system is capable of notifying and storing information.  The dashboard is designed to help fleet managers and operators efficiently track and manage their vehicles.

## Installation
If you already have the necessary tools installed, you can skip step 1.

### Step 1: Prerequisites

You need the following programs/tools:

1. **Git Bash Terminal** - Follow the steps provided [here] https://git-scm.com/downloads .
2. **Docker** - Follow the installation instructions [here] https://docs.docker.com/engine/install/.

### Step 2: Open Git Bash Terminal

1. **Navigate to the location where you want to set up your project**:
    ```bash
    cd PATH_TO_YOUR_WORKSPACE
    ```

2. **Clone the project**:
    ```bash
    git clone https://collaborating.tuhh.de/e-19/teaching/bd24_project_m8_b.git
    ```

## Usage
Before proceeding, ensure that Docker is running.

### Step 1: Start the Project

1. **Open Git Bash Terminal and navigate to the folder where you cloned the project**:
    ```sh
    cd PATH_TO_THE_PROJECT
    ```

2. **Run the following command**:
    ```sh
    docker-compose up -d
    ```
    > Starting with Docker Compose v2 (or later versions), you can omit the hyphen and use docker compose up -d instead of docker-compose up -d.

### Step 2: Open the Project

1. **Open your preferred browser**.

2. **Go to the following URL to view the dashboard**:
    ```sql
   localhost:5601/app/dashboards#/view/aea780f0-1ee2-11ef-a2ca-172534fb526f?embed=true&_g=(refreshInterval:(pause:!f,value:5000),time:(from:now-7d%2Fd,to:now))&hide-filter-bar=true
    ```
    
### Step 3: Close the project

1. **Inside the same gitbash Terminal run the following command**
    ```sh
    docker compose down
    ```
  

## Support
### About Us

We are master's students passionate about data science, software engineering, and real-time systems. This project, TIME (Taxi Information and Monitoring Engine), is a result of our collaborative efforts to apply our skills in creating a practical and impactful tool for fleet management.

### Getting Help

If you encounter any issues or have questions about the project, there are several ways to get support:

#### Email:

- You can reach out to us via email at [timetaxidash@gmail.com](mailto:timetaxidash@gmail.com). We will do our best to respond promptly.



## Feature: Real-time Analytics
**Version 2.0**

### Feature: Machine Learning Integration
- Add machine learning models to predict trends and anomalies in data.
- Integrate ML workflows using frameworks like TensorFlow or PyTorch.

### Improvement: Scalability
- Implement auto-scaling for the Kafka broker and Flink applications.
- Use Kubernetes for container orchestration to handle increased load.

**Version 2.1**

### Feature: Enhanced Security
- Implement user authentication and authorization for Kibana and Elasticsearch.
- Encrypt data in transit and at rest.

### Improvement: User Experience
- Refine the dashboard UI/UX for better usability.
- Add customizable widgets and reports.

## Horizontal Scaling

### Kafka Brokers
- Add more Kafka brokers to distribute the load.

### Flink Nodes
- Increase the number of Flink nodes to handle more data streams.

### Elasticsearch Nodes
- Add more Elasticsearch nodes for better query performance and data indexing.

## Vertical Scaling

### Increase Resource Allocation
- Allocate more CPU and memory to containers running critical services like Kafka, Flink, and Elasticsearch.

### Optimized Configurations
- Tune configuration parameters for Kafka, Flink, and Elasticsearch to maximize performance.

## Container Orchestration

### Kubernetes
- Deploy the entire stack on Kubernetes to manage container scaling, load balancing, and automated deployments.

### Helm Charts
- Create Helm charts for easy deployment and management of the Kubernetes cluster.

## High Availability

### Redundant Services
- Ensure high availability by running redundant instances of critical services.

### Failover Mechanisms
- Implement failover mechanisms to automatically switch to backup services in case of failures.

## Additional Enhancements

### Monitoring and Logging
- Integrate monitoring tools like Prometheus and Grafana to visualize system performance.
- Implement centralized logging using the ELK stack (Elasticsearch, Logstash, Kibana).

### Data Backup and Recovery
- Set up automated backup processes for critical data stored in Kafka and Elasticsearch.
- Implement data recovery procedures to restore services quickly in case of data loss.

### Documentation and Tutorials
- Provide comprehensive documentation for setup, usage, and troubleshooting.
- Create video tutorials and walkthroughs to help new users get started with the project.

## Contributing
Contributions are welcome! Please follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
    ```sh
    git checkout -b feature/YourFeature
    ```
3. **Commit your changes**:
    ```sh
    git commit -m 'Add some feature'
    ```
4. **Push to the branch**:
    ```sh
    git push origin feature/YourFeature
    ```
5. **Create a new Pull Request**.


## Authors and acknowledgment
This project was developed by a team of four master's students:

- **Aman Kumar**
- **Arpit Pandey**
- **Saina Pattanayak**
- **Yussra Hussein**

### Acknowledgements

We would like to express our gratitude to the following individuals and organizations for their support and contributions:

- **Our professors and mentors** for their guidance and invaluable feedback.
- **Our classmates** for their encouragement and collaboration.
- **Open source community** for the tools and libraries that made this project possible.
- **Friends and family** for their constant support and understanding.

We hope this project, TIME (Taxi Information and Monitoring Engine), is a useful tool for fleet management and demonstrates the skills and knowledge we gained during our master's program.


## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software as long as you include the original copyright and license notice in any copy of the software you create or distribute.

**MIT License**


