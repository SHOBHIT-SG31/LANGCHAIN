from langchain_text_splitters import RecursiveCharacterTextSplitter
text="""
The world is a vast and diverse place, filled with countless cultures, landscapes, and histories. From the snowy peaks of the Himalayas to the endless deserts of the Sahara, every corner of the Earth tells a unique story. Humanity has built civilizations that rose and fell, leaving behind monuments, traditions, and knowledge that continue to inspire generations. The world is not just about geography—it is also about the people who inhabit it, each contributing to the rich tapestry of human experience.

In today's era, the world feels smaller than ever before. Technology connects distant nations within seconds, allowing ideas, art, and innovations to travel across borders effortlessly. Yet, despite this interconnectedness, the world remains beautifully complex, with languages, beliefs, and customs that remind us of our differences and similarities. It is a place of constant change, where challenges like climate change and inequality coexist with opportunities for progress and unity.

Ultimately, the world is both fragile and resilient. It is a shared home that requires care, respect, and cooperation. Whether through science, culture, or compassion, humanity has the power to shape the future of this planet, ensuring that its beauty and diversity continue to thrive for generations to come."""
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)
chunks = splitter.split_text(text) 
print(len(chunks))
print(chunks)