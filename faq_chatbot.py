faq = {
"what is ai": "AI means Artificial Intelligence.",
"what is python": "Python is a programming language."
}

question = input("Ask a question: ").lower()

if question in faq:
    print("Bot:", faq[question])
else:
    print("Bot: Sorry, I don't know the answer.")