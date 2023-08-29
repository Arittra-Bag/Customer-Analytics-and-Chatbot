import pandas as pd
import re

# Load the customer data from a CSV file
customer_data = pd.read_csv('/kaggle/input/customer-segmentation/Mall_Customers.csv')

# Configure pandas display options to center-align the columns
pd.set_option('colheader_justify', 'center')

print("Chatbot: Hi! I can help you find spending scores for mall customers.")
print("Chatbot: You can ask questions like:")
print("Chatbot: - 'Spending Score for male customers aged 19-25'")
print("Chatbot: - 'Spending Score for female customers aged 30-40'")
print("Chatbot: - 'Exit' to end the conversation")

# Fixed input for testing
user_input = "spending score for male customers aged 19-25"

if user_input == "exit":
    print("Chatbot: Goodbye!")
else:
    if "spending score for" in user_input:
        # Parse the user's query and extract relevant information
        query_parts = user_input.split("for")
        if len(query_parts) == 2:
            _, conditions = query_parts
            conditions = conditions.strip()
            
            # Initialize filters
            gender = None
            age_range = None
            
            # Extract gender and age range
            if "female" in conditions:
                gender = "Female"
            elif "male" in conditions:
                gender = "Male"
            else:
                print("Chatbot: Invalid gender. Please specify 'male' or 'female'.")
            
            # Use regular expression to extract age range
            age_range_match = re.search(r'aged (\d+)-(\d+)', conditions)
            if age_range_match:
                age_start = int(age_range_match.group(1))
                age_end = int(age_range_match.group(2))
                age_range = [age_start, age_end]
            
            # Filter the data based on the user's query
            if gender and age_range:
                filtered_data = customer_data[(customer_data['Gender'] == gender) & 
                                              (customer_data['Age'] >= age_range[0]) &
                                              (customer_data['Age'] <= age_range[1])]
                
                # Print the results in a table format with centered alignment
                if not filtered_data.empty:
                    print(f"Chatbot: Here are the spending scores for {gender} customers aged {age_range[0]}-{age_range[1]}:")
                    print(filtered_data[['CustomerID', 'Spending Score (1-100)']].to_string(index=False))
                else:
                    print("Chatbot: No matching records found.")
            else:
                print("Chatbot: Invalid query format. Please specify gender and age range.")
        else:
            print("Chatbot: Invalid query format. Please use 'Spending Score for [gender] customers aged [start]-[end]'.")
    else:
        print("Chatbot: I don't understand that. Please try again.")