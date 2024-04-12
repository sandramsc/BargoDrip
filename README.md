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

