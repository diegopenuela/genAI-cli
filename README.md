# genAI-cli
genAI-CLI is an experimental Python-based Command Line Interface (CLI) tool designed to access Generative AI features from AI platforms like Hugging Face.

# MyCLI Tool

MyCLI is a Python-based Command Line Interface (CLI) tool designed to [briefly describe the main purpose or functionality of your CLI].

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Testing](#testing)
- [License](#license)
- [Contact](#contact)

## Installation
To use genAI-CLI, follow these steps:

1. **Clone the Repository:**
git clone https://github.com/diegopenuela/genAI-cli
cd genAI-cli

2. **Build the Docker Image:**
docker build -t genai-cli-image .

3. **Run the CLI:**
docker run -it genai-cli-image /bin/bash

## Usage
MyCLI provides the following commands:

- `dummy arg1 arg2`: Dummy commands that receives a string argument and a integer argument

Example:
python app.py dummy falcon 9

## Configuration

You can configure genAI-CLI by setting environment variables:

- `DEPLOYMENT_ENV`: Set to "development" for local development or "production" for production.
- `API_KEY`: Your API key for authentication.
- `API_SECRET`: Your API secret for authentication.

Make sure to create a `.env` file and populate it with the necessary values for your environment.

## Deployment

genAI-CLI can be deployed locally using Docker. For production deployment, will involve creating executable packages that users can install and run on their local machines.

## Contributing

We welcome contributions to MyCLI! To contribute:

1. [Fork](https://github.com/diegopenuela/genAI-cli/fork) the repository.
2. Create a new branch: `git checkout -b feature/my-feature`.
3. Make your changes and commit them: `git commit -m "Add new feature"`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Submit a pull request.

## Testing

To run tests for genAI-CLI, use the following command:

python -m unittest discover tests

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, feel free to reach out to us at [diego.penuela@gmail.com](mailto:diego.penuela@gmail.com).




