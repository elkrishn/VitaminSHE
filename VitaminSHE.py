import nltk; nltk.download('popular')


# Essential Vitamins (all in milligrams): {"Age Range": (darily required intake)}
vitamin_a = {"1-3": 0.600, "4-8": 0.900, "9-13": 1.7, "14-18": 2.8, "19-30": 3.0, "31-50": 3.0, "51-70": 3.0, "71+": 3.0}
vitamin_e = {"1-3": 200, "4-8": 300, "9-13": 600, "14-18": 800, "19-30": 1000, "31-50": 1000, "51-70": 1000, "71+": 1000}
vitamin_c = {"1-3": 400, "4-8": 650, "9-13": 1200, "14-18": 1800, "19-30": 2000, "31-50": 2000, "51-70": 2000, "71+": 2000}
vitamin_d = {"1-3": 0.063, "4-8": 0.090, "9-13": 0.017, "14-18": 0.028, "19-30": 3.0, "31-50": 3.0, "51-70": 3.0, "71+": 3.0}

vitamin_b_6 = {"1-3": 0.030, "4-8": 0.040, "9-13": 0.060, "14-18": 0.080, "19-30": 0.100, "31-50": 0.100, "51-70": 0.100, "71+": 0.100}
vitaminb_b_12 = {"1-3": 0.0009, "4-8": 0.0012, "9-13": 0.0018, "14-18": 0.0024, "19-30": 0.0024, "31-50": 0.0024, "51-70": 0.0024, "71+": 0.0024}
# Does not factor in pregnancy and breastfeeding at the moment


# Essential Minerals (all in milligrams): {"Age Range": (daily required intake)
calcium = {"1-3": 0.700, "4-8": 1.000, "9-13": 1.300, "14-18": 1.300, "19-30": 1.000, "31-50": 1.000, "51-70": 1.200, "71+": 1.200}
iron = {"1-3": 7, "4-8": 10, "9-13": 8, "14-18": 15, "19-30": 18, "31-50": 18, "51-70": 8, "71+": 8}
magnesium = {"1-3": 80, "4-8": 130, "9-13": 240, "14-18": 360, "19-30": 310, "31-50": 320, "51-70": 320, "71+": 320}
potassium = {"1-3": 2000, "4-8": 2300, "9-13": 2300, "14-18": 2300, "19-30": 2600, "31-50": 2600, "51-70": 2600, "71+": 2600}
zinc = {"1-3": 3, "4-8": 5, "9-13": 8, "14-18": 9, "19-30": 8, "31-50": 8, "51-70": 8, "71+": 8}
# Does not factor in pregnancy and breastfeeding at the moment

#Symptoms of Vitamin and Mineral Deficiency 
vitamin_a_symptoms = """dry eyes, dry skin, frequent infections, spots in the eyeball, inability to see in dim light"""
"""
vitamin_a_deficiency  = poor night vision, dry eyes dry skin, frequent infections, 'spots in the eyes'] 
vitamin_b_6_deficiency = ['depression', 'numbness', 'anemia']
vitamin_b_12_deficiency = ['depression', 'poor concentration', 'numbness']
vitamin_c_deficiency = ['depression', 'bruising', 'fatigue', 'bleeding gums', 'tooth loss']
vitamin_d_deficiency = ['twitching', 'muscle pain and cramps', 'irregular menstruation', 'weak bones', 'hair loss', 'high blood pressure']
vitamin_e_deficiency = ['unsteady movement or walking']

calcium_deficiency = ['twitching', 'muscle cramping', 'twitching', 'spasms']
iron_deficiency = ['poor concentration', 'irregular menstruation', 'fatigue', 'anemia']
magnesium_deficiency = ['palpitations', 'constipation', 'twitching', 'muscle pain and cramps']
potassium_deficiency = ['palpitations', 'constipation', 'muscle pain and cramps']
zinc_deficiency = ['poor night vision', 'loss of appetite', 'loss of taste', 'hair loss', 'diarrhea']
"""
# Creates a user 
class User:
    def __init__(self, name=str, age=int, height=int, weight=int, pregnancy_status=str, breastfeeding_status=str, user_symptoms=str):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.pregnancy_status = pregnancy_status
        self.breastfeeding_status = breastfeeding_status
        self.user_symptoms = user_symptoms
        self.age_range = self.compute_age_range()
        
        self.user_vitamin_a = vitamin_a[self.age_range]
        self.user_vitamin_b_6 = vitamin_b_6[self.age_range]
        self.user_vitamin_b_12 = vitaminb_b_12[self.age_range]
        self.user_vitamin_c = vitamin_c[self.age_range]
        self.user_vitamin_d = vitamin_d[self.age_range]
        self.user_vitamin_e = vitamin_e[self.age_range]

        
        self.user_calcium = calcium[self.age_range]
        self.user_iron = iron[self.age_range]
        self.user_magnesium = magnesium[self.age_range]
        self.uesr_potassium = potassium[self.age_range]
        self.user_zinc = zinc[self.age_range]
        
    
    def compute_age_range(self):
        """Figures out an age range for the user"""

        # Checks if user is in the age range of 1 to 3
        if self.age < 0 & self.age >= 3:
            self.age_range = "1-3"
        
        # Checks if user is in the age range of 4 to 8
        if self.age >= 4 & self.age <= 8:
            self.age_range = "4-8"
        
        # Checks if user is in the age range of 9 to 13
        if self.age >= 9 & self.age <= 13:
            self.age_range = "9-13"
        
        # Checks if user is in the age range of 14 to 18
        if self.age >= 14 & self.age <= 18:
            self.age_range = "14-18"

        # Checks if user is in the age range of 19 to 30
        if self.age >= 19 & self.age <= 30:
            self.age_range = "19-30"
        
        # Checks if user is in the age range of 31 to 50
        if self.age >= 31 & self.age <= 50:
            self.age_range = "31-50"
        
        # Checks if user is in the age range of 51 to 70
        if self.age >= 51 & self.age <= 70:
            self.age_range = "51-70"
        
        # Checks if user is in the age range of 71+
        if self.age >= 71:
            self.age_range = "71+"
        
        return self.age_range

    
    def analyze_symptoms(self):
        keywords = nltk.word_tokenize(self.user_symptoms)
        v_a_counter = 0
        v_b_6_counter = 0
        v_b_12_counter = 0
        v_c_counter = 0
        v_d_counter = 0
        v_e_counter = 0

        calcium_counter = 0
        iron_counter = 0
        magnesium_counter = 0
        potassium_counter = 0
        zinc_counter = 0


        for k in keywords:

            if k in vitamin_a_deficiency:
                v_a_counter += 1

            if k in vitamin_b_6_deficiency:
                v_b_6_counter += 1
            
            if k in vitamin_b_12_deficiency:
                v_b_12_counter += 1

            if k in vitamin_c_deficiency:
                v_c_counter += 1

            if k in vitamin_d_deficiency:
                v_d_counter += 1

            if k in vitamin_e_deficiency:
                v_e_counter += 1
            
            if k in calcium_deficiency:
                calcium_counter += 1
            
            if k in iron_deficiency:
                iron_counter += 1
            
            if k in magnesium_deficiency:
                magnesium_counter += 1
            
            if k in potassium_deficiency:
                potassium_counter += 1
            
            if k in zinc_deficiency:
                zinc_counter += 1
            
        results = {"Vitamin A": v_a_counter, "Vitamin B6": v_b_6_counter, "Vitamin B12": v_b_12_counter, "Vitamin C": v_c_counter, 
        "Vitamin D": v_d_counter, "Vitamin E": v_e_counter, "Calcium": calcium_counter, 
        "Iron": iron_counter, "Magnesium": magnesium_counter, "Potassium": potassium_counter, "Zinc": zinc_counter}
        
        
        
        
        return keywords
        

    def get_status(self):
        
        """Returns the basic information of the user"""

        status = """
-----------------GENERAL USER INFO-----------------
                 Name: {name}
                 Age: {age}
                 Age Range: {age_range}
                 Height: {height}
                 Weight: {weight}
                 Pregnancy Status: {pregnancy_status}
                 Breastfeeding Status: {breastfeeding_status}

-----------------USER'S RECOMMENDED DAILY VITAMIN AND MINERAL COUNT-------------
                                (in milligrams, mg)
                 Vitamin A: {user_vitamin_a}
                 Vitamin B6: {user_vitamin_b_6}
                 Vitamin B12: {user_vitamin_b_12}
                 Vitamin C: {user_vitamin_c}
                 Vitamin D: {user_vitamin_d}
                 Vitamin E: {user_vitamin_e}
                 
                 Calcium: {user_calcium}
                 Iron: {user_iron}
                 Magnesium: {user_magnesium}
                 Potassium: {user_potassium}
                 Zinc: {user_zinc}
                 """
        return status.format(name=self.name, age=self.age, age_range=self.age_range, height=self.height, weight=self.weight, pregnancy_status=self.pregnancy_status, 
        breastfeeding_status=self.breastfeeding_status, user_vitamin_a=self.user_vitamin_a,
        user_vitamin_b_6=self.user_vitamin_b_6, user_vitamin_b_12=self.user_vitamin_b_12, user_vitamin_c=self.user_vitamin_c, user_vitamin_d=self.user_vitamin_d, user_vitamin_e=self.user_vitamin_e,
        user_calcium=self.user_calcium, user_iron=self.user_iron, user_magnesium=self.user_magnesium, user_potassium=self.uesr_potassium, user_zinc=self.user_zinc)
        

# Asks survey questions and calls on functions that will narrow down data and deficencies
def main():
    # Gets user information through a series of questions
    print("Welcome to VitaminSHE!")
   
    user_name = input("What is your name? ")
    
    user_age = int(input("How old are you? "))
   
    # Checks if user_age is a valid input
    while user_age <= 0:
        print("Invalid Entry.")
        user_age = int(input("What is your name? "))

    user_height = input("What is your height (Please round to the nearest whole inch)? ")
    user_weight = input("What is your weight? (Please round to the nearest whole pound)? ")

    pregnancy_status = input("Are you pregnant (Y or N)? ")
    pregnancy_status = pregnancy_status.upper()
    
    # Checks if pregnancy_status is a valid input
    while pregnancy_status != "Y" and pregnancy_status != "N":
        print("Invalid Entry.")
        pregnancy_status = input("Are you pregnant (Y or N)? ")
        pregnancy_status = pregnancy_status.upper()

    breastfeeding_status = input("Are you currently breastfeeding (Y or N)? ")
    breastfeeding_status = breastfeeding_status.upper()

    # Checks if breastfeeding_status is a valid input
    while breastfeeding_status != "Y" and breastfeeding_status != "N":
        print("Invalid Entry.")
        breastfeeding_status = input("Are you pregnant (Y or N)? ")
        breastfeeding_status = breastfeeding_status.upper()

    print("\nDo you think you could be vitamin or mineral deficient?")
    user_symptoms = input("In one paragraph, please describe any symptoms you are feeling or noticing (i.e. fatigue, unsteady walking or movement, etc.): ")
    
    user = User(user_name, user_age, user_height, user_weight, pregnancy_status, breastfeeding_status, user_symptoms)
    print(user.analyze_symptoms())
    print(user.get_status())

main()
