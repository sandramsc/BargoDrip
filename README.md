# BargoDrip

## Application Description

BargoDrip is a command-line tool designed to help users find the cheapest prices for products across different stores in their area. It provides features to retrieve current stock data from stores, compare prices, and suggest the cheapest option along with the address of the corresponding store.

## Table of Contents

<details>
<summary>Table of Contents</summary>

- [BargoDrip](#bargodrip)
- [Application Description](#application-description)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

</details>

## Video Demo

[link](https://link.com)

## Screenshots

## Technology Stack

| Technology | Description              |
| ---------- | ------------------------ |
| Python     | Programming Language     |
| BeautifulSoup | Web scraping library |
| Google Maps API | API for retrieving store locations |

### Features

1. Retrieve current stock data from stores in a specified area.
2. Compare prices across different stores for a given product.
3. Suggest the cheapest option and display the address of the corresponding store.

It's great to include a "Challenges" section in your README.md file to provide transparency about the potential hurdles faced during the development process. Here's an example of how you can structure this section:

## Challenges

Developing BargoDrip presented several challenges, including:

1. **Data Acquisition:** Obtaining accurate and up-to-date data from various stores and APIs posed a challenge due to the lack of standardized data formats and inconsistent APIs. Overcoming this challenge required extensive research into data sources and thorough data validation processes.

2. **User Interface Design:** Designing an intuitive and user-friendly command-line interface (CLI) that caters to both beginner and intermediate users was challenging. Balancing simplicity with functionality while ensuring a seamless user experience required iterative design iterations and user testing.

3. **Integration of External APIs:** Integrating external APIs to retrieve store names, product items, and other relevant information presented challenges, particularly in handling authentication, rate limits, and error handling. Overcoming this challenge involved careful API selection, thorough documentation review, and robust error handling mechanisms.

4. **Performance Optimization:** Optimizing the performance of the CLI tool, especially when fetching and processing large datasets, posed challenges in terms of response times and resource utilization. Implementing efficient algorithms, asynchronous processing, and caching strategies helped address these performance concerns.

5. **Deployment and Packaging:** Setting up deployment pipelines and packaging the CLI tool for distribution across different platforms (Windows, macOS, Linux) posed challenges in ensuring compatibility and seamless installation experiences. Overcoming this challenge required knowledge of packaging tools and scripting languages.

## Lessons Learned

Through overcoming these challenges, several valuable lessons were learned:

1. **Thorough Planning and Research:** Investing time in thorough planning and research upfront can mitigate potential challenges down the line. Understanding the project requirements, available resources, and potential pitfalls early on is crucial for successful project execution.

3. **Collaboration and Support:** Leveraging the expertise and support of peers, online communities, and developer forums proved invaluable in overcoming technical challenges. Collaborating with others, seeking advice, and sharing knowledge fosters a sense of community and accelerates problem-solving.

4. **Persistence and Adaptability:** Persistence and adaptability are key qualities when facing complex challenges in software development. Embracing failures as learning opportunities, staying resilient in the face of setbacks, and remaining open to alternative solutions are essential for overcoming obstacles and achieving success.

## Installation

1. Clone the repository:
```bash
$ git clone https://github.com/your-username/BargoDrip.git
```
## Getting Started

### Prerequisites
- Go installed on your local machine

### Installation
1. Navigate to the project directory:
    ```bash
    $ cd BargoDrip
    ```

2. Fill in the required environment variables by creating a `.env` file based on the provided `.env.example`.

3. Start the application:
    ```bash
    $ go run main.go
    ```
### If using Docker:

Build the Docker image:

```bash
$ docker build -t bargodrip .
```

Run the Docker container:

```bash
$ docker run -it --rm bargodrip
```

### Usage
```bash
$ bargodrip search "iPhone 11" --area "New York"
```
```bash
Searching for "iPhone 11" in New York...

Store: Best Tech
Price: $999
Address: 123 Main St, New York, NY
Opening Hours: Mon-Sat 9:00 AM - 8:00 PM, Sun 10:00 AM - 6:00 PM

Store: Mobile Express
Price: $899
Address: 456 Elm St, New York, NY
Opening Hours: Mon-Sat 10:00 AM - 7:00 PM, Sun 11:00 AM - 5:00 PM

Store: Electronics Hub
Price: $949
Address: 789 Oak St, New York, NY
Opening Hours: Mon-Fri 8:00 AM - 9:00 PM, Sat-Sun 9:00 AM - 8:00 PM

Store: Tech Emporium
Price: $899
Address: 101 Maple St, New York, NY
Opening Hours: Mon-Sat 9:30 AM - 7:30 PM, Sun 11:00 AM - 6:00 PM

Store: Gadget Galaxy
Price: $949
Address: 202 Pine St, New York, NY
Opening Hours: Mon-Sun 10:00 AM - 8:00 PM

Store: Mega Mart
Price: $899
Address: 303 Cedar St, New York, NY
Opening Hours: Mon-Fri 9:00 AM - 9:00 PM, Sat-Sun 10:00 AM - 7:00 PM

Cheapest option: Mobile Express ($899)
```


## Contributing

We welcome contributions from the community! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## Authors

| Name            | Link                                        |
| --------------- | ------------------------------------------- |
| Sandra Ashipala | https://www.linkedin.com/in/sandraashipala/ |

## License

[![GitLicense](https://img.shields.io/badge/License-MIT-lime.svg)](https://github.com/sandramsc/BargoDrip/blob/master/LICENSE.md)

