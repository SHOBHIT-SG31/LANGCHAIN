from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# from langchain_core.documents import Document

doc1  = Document(page_content="Virat Kohli is a right-handed batsman.", 
                 metadata={"team": "Royal Challengers Bangalore", "role": "Batsman"})

doc2  = Document(page_content="MS Dhoni is a wicket-keeper batsman and captain.", 
                 metadata={"team": "Chennai Super Kings", "role": "Wicket-Keeper"})

doc3  = Document(page_content="Rohit Sharma is an opening batsman and captain.", 
                 metadata={"team": "Mumbai Indians", "role": "Batsman"})
 
doc4  = Document(page_content="Jasprit Bumrah is a fast bowler.", 
                 metadata={"team": "Mumbai Indians", "role": "Bowler"})

doc5  = Document(page_content="Hardik Pandya is an all-rounder.", 
                 metadata={"team": "Mumbai Indians", "role": "All-Rounder"})

doc6  = Document(page_content="KL Rahul is a batsman and wicket-keeper.", 
                 metadata={"team": "Lucknow Super Giants", "role": "Batsman/WK"})

doc7  = Document(page_content="Shubman Gill is a top-order batsman.", 
                 metadata={"team": "Gujarat Titans", "role": "Batsman"})

doc8  = Document(page_content="Rashid Khan is a leg-spin bowler.", 
                 metadata={"team": "Gujarat Titans", "role": "Bowler"})

doc9  = Document(page_content="David Warner is an opening batsman.", 
                 metadata={"team": "Delhi Capitals", "role": "Batsman"})

doc10 = Document(page_content="Rishabh Pant is a wicket-keeper batsman.", 
                 metadata={"team": "Delhi Capitals", "role": "Wicket-Keeper"})

doc11 = Document(page_content="Sanju Samson is a wicket-keeper batsman and captain.", 
                 metadata={"team": "Rajasthan Royals", "role": "Wicket-Keeper"})

doc12 = Document(page_content="Yuzvendra Chahal is a leg-spin bowler.", 
                 metadata={"team": "Rajasthan Royals", "role": "Bowler"})

doc13 = Document(page_content="Andre Russell is an explosive all-rounder.", 
                 metadata={"team": "Kolkata Knight Riders", "role": "All-Rounder"})

doc14 = Document(page_content="Sunil Narine is a spinner and pinch-hitter.", 
                 metadata={"team": "Kolkata Knight Riders", "role": "Bowler/All-Rounder"})

doc15 = Document(page_content="Shikhar Dhawan is an opening batsman and captain.", 
                 metadata={"team": "Punjab Kings", "role": "Batsman"})

doc16 = Document(page_content="Arshdeep Singh is a left-arm fast bowler.", 
                 metadata={"team": "Punjab Kings", "role": "Bowler"})

doc17 = Document(page_content="Faf du Plessis is a batsman and captain.", 
                 metadata={"team": "Royal Challengers Bangalore", "role": "Batsman"})

doc18 = Document(page_content="Glenn Maxwell is an all-rounder.", 
                 metadata={"team": "Royal Challengers Bangalore", "role": "All-Rounder"})

doc19 = Document(page_content="Mohammed Shami is a fast bowler.", 
                 metadata={"team": "Gujarat Titans", "role": "Bowler"})

doc20 = Document(page_content="Dinesh Karthik is a wicket-keeper batsman.", 
                 metadata={"team": "Royal Challengers Bangalore", "role": "Wicket-Keeper"})
