# Text Summarization with BART

A short Python script that uses Hugging Face's `facebook/bart-large-cnn` model to summarize text. The example summarizes the famous opening paragraph of Charles Dickens' *A Tale of Two Cities*.

## Features

- Uses a state‑of‑the‑art summarization model (BART).
- Simple, single‑file implementation.
- Minimal dependencies – just Transformers and PyTorch.
- Ready‑to‑run with a built‑in example.

## Requirements

- Python 3.8+
- PyTorch
- Hugging Face Transformers

Install them with:

```bash
pip install torch transformers
```

## Installation

1. Clone the repository or download `main.py`.
2. Install the dependencies (see above).
3. Run the script – the model will be downloaded automatically on first run.

## Usage

```bash
python main.py
```

The script will:
1. Load the summarization model (downloading ~1.6 GB on first run).
2. Print the original long text.
3. Generate and print a concise summary.

## Example Output

```
Loading summarization model... (first time takes a minute)
============================================================
ORIGINAL TEXT:
============================================================

It was the best of times, it was the worst of times, it was the age of wisdom, 
it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, 
it was the season of Light, it was the season of Darkness, it was the spring of hope, 
it was the winter of despair, we had everything before us, we had nothing before us, 
we were all going direct to Heaven, we were all going direct the other way—in short, 
the period was so far like the present period, 
that some of its noisiest authorities insisted on its being received, 
for good or for evil, in the superlative degree of comparison only. - Charles Dickens' A Tale of Two Cities

Generating summary...

============================================================
SUMMARY:
============================================================
The period was so far like the present period that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.
============================================================
```

## Customisation

- **Change the input text** – Replace the `text` variable with your own text.
- **Adjust summary length** – Modify the `max_length` and `min_length` parameters in the `summarizer()` call.
- **Use a different model** – Change the model name in the `pipeline()` call (e.g., `"t5-small"`, `"google/pegasus-xsum"`). Check Hugging Face Hub for options.

## File Structure

```
.
├── main.py        # Complete summarization script
└── README.md      # This file
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hugging Face for the Transformers library and model.
- Facebook AI for the BART model.
