import typer
from transformers import pipeline

app = typer.Typer()

@app.command()
def sentiment_analysis(text: str):
    # Load the sentiment-analysis pipeline from Hugging Face
    sentiment_classifier = pipeline("sentiment-analysis")

    # Perform sentiment analysis on the input text
    result = sentiment_classifier(text)

    # Extract the sentiment label and score
    sentiment_label = result[0]["label"]
    sentiment_score = result[0]["score"]

    # Print the sentiment analysis results
    typer.echo(f"Sentiment Analysis Result:")
    typer.echo(f"Text: {text}")
    typer.echo(f"Sentiment Label: {sentiment_label}")
    typer.echo(f"Sentiment Score: {sentiment_score}")
