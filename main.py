# pip install transformers torch

from transformers import pipeline

print("Loading summarization model... (first time takes a minute)")

# Load summarization model from Hugging Face
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Text to summarize
text = """
It was the best of times, it was the worst of times, it was the age of wisdom, 
it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, 
it was the season of Light, it was the season of Darkness, it was the spring of hope, 
it was the winter of despair, we had everything before us, we had nothing before us, 
we were all going direct to Heaven, we were all going direct the other way—in short, 
the period was so far like the present period, 
that some of its noisiest authorities insisted on its being received, 
for good or for evil, in the superlative degree of comparison only. - Charles Dickens' A Tale of Two Cities
"""

print("=" * 60)
print("ORIGINAL TEXT:")
print("=" * 60)
print(text)

# Generate summary
print("\nGenerating summary...")
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)

print("\n" + "=" * 60)
print("SUMMARY:")
print("=" * 60)
print(summary[0]['summary_text'])
print("=" * 60)