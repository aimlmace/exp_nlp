from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import csv

# Create a chatbot instance
chatbot = ChatBot(
    "SimpleBot",
    # storage_adapter="chatterbot.storage.SQLStorageAdapter",  # Uses SQLite
    # database_uri="sqlite:///:memory:",  # In-memory storage (not saved after restart)
    # logic_adapters=[
    #     "chatterbot.logic.BestMatch",
    # ]
)

# First, train on the built-in English corpus using ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")  # Train using the English corpus

# Now, use ListTrainer for custom data
trainer_list = ListTrainer(chatbot)

# Custom data as a list of tuples (question, response)
custom_training_data = [
    "What is the abbreviation for Mar Athanasius College of Engineering?", "Mar Athanasius College of Engineering is abbreviated as MACE.",
    "When was MACE established?", "MACE was established in 1961.",
    "Where is MACE located?", "MACE is located in Kothamangalam, Kerala.",
    "What is the managing body of MACE?", "MACE is managed by the Mar Athanasius College Association.",
    "Which university is MACE affiliated with?", "MACE is affiliated with APJ Abdul Kalam Technological University.",
    "Is MACE approved by AICTE?", "Yes, MACE is approved by the All India Council for Technical Education (AICTE).",
    "What undergraduate programs does MACE offer?", "MACE offers B.Tech programs in Civil Engineering, Mechanical Engineering, Electrical & Electronics Engineering, Electronics & Communication Engineering, Computer Science and Engineering, Data Science, and Artificial Intelligence and Machine Learning.",
    "What postgraduate programs does MACE offer?", "MACE offers M.Tech programs in Computer Science and Engineering, Computer Aided Structural Engineering, Production & Industrial Engineering, Power Electronics, VLSI, and Thermal Power Engineering, as well as a Master of Computer Applications (MCA) program.",
    "Are the undergraduate courses at MACE accredited?", "Yes, all undergraduate courses at MACE are accredited by the National Board of Accreditation (NBA).",
    "What is the size of the MACE campus?", "The campus of MACE spans over 62 acres.",
    "What sports facilities are available at MACE?", "MACE offers a 50-meter swimming pool, football and cricket grounds, indoor and outdoor badminton courts, basketball and tennis courts, a volleyball court, a gymnasium, and table tennis facilities.",
    "Does MACE provide hostel facilities?", "Yes, MACE provides separate hostel accommodations for boys and girls, each with attached dining facilities.",
    "What technical fest is organized by MACE?", "MACE organizes an annual technical fest called 'Takshak'.",
    "What cultural fest is organized by MACE?", "MACE organizes an annual cultural fest called 'Sanskriti'.",
    "What student clubs are active at MACE?", "Active student clubs at MACE include IEEE, ASME, SAE, IEDC, MACE Music Club, MACE Dance Club (MadC), and Divaat (fashion club).",
    "Who is a notable alumnus of MACE in the field of space research?", "Dr. S Unnikrishnan Nair, Director of the Vikram Sarabhai Space Centre, is a notable alumnus of MACE.",
    "Who is a notable alumnus of MACE in the United Nations?", "Murali Thummarukudy, Chief of Disaster Risk Reduction in the UN Environment Programme, is a notable alumnus of MACE.",
    "Who is the founder of IBS Software Services and an alumnus of MACE?", "V. K. Matthews, the founder and chairman of IBS Software Services, is an alumnus of MACE.",
    "Which Malayalam film director is an alumnus of MACE?", "Ranjith Sankar, a Malayalam screenwriter and film director, is an alumnus of MACE.",
    "How many faculty members does MACE have?", "MACE has approximately 151 faculty members.",
    "How many engineering departments are there at MACE?", "There are six main engineering departments at MACE.",
    "Where can information about the Mechanical Engineering faculty at MACE be found?", "Information about the Mechanical Engineering faculty can be accessed on the official MACE website.",
    "Does the Civil Engineering department at MACE have a research center?", "Yes, the Civil Engineering department has a dedicated research center with specialized faculty in areas like Structural Engineering and Concrete Technology.",
    "Where can information about the Electrical & Electronics Engineering faculty at MACE be found?", "Faculty information for the Electrical & Electronics Engineering department is available on the department's section of the MACE website.",
    "Where can information about the Electronics & Communication Engineering faculty at MACE be found?", "Details about the Electronics & Communication Engineering faculty can be found on the official MACE website.",
    "Where can information about the Computer Science & Engineering faculty at MACE be found?", "Faculty profiles for the Computer Science & Engineering department are listed on the department's page of the MACE website.",
    "Where can information about the Computer Applications faculty at MACE be found?", "Information about the Computer Applications faculty is available on the MACE website.",
    "What are the qualifications of the faculty at MACE?", "Many faculty members at MACE hold advanced degrees, including Ph.Ds., from reputed institutions.",
    "What is the experience level of the faculty at MACE?", "Faculty members at MACE bring a wealth of experience in teaching, research, and industry collaborations.",
    "Are there active research centers at MACE?", "Yes, several departments at MACE have active research centers, with faculty leading projects in cutting-edge areas of engineering and technology.",
    "How do students rate the faculty at MACE?", "Students have positively reviewed the faculty at MACE, noting their qualifications, helpfulness, and subject knowledge.",
]



# Train with the custom data using ListTrainer
trainer_list.train(custom_training_data)

# Start a conversation loop
print("\nSimpleBot: Hello! Type 'exit' to stop the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("SimpleBot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print(f"SimpleBot: {response}")
