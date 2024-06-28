import re
import getpass

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    upper_case_criteria = bool(re.search(r'[A-Z]', password))
    lower_case_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    criteria_met = sum([length_criteria, upper_case_criteria, lower_case_criteria, number_criteria, special_char_criteria])
    
    if criteria_met == 5:
        strength = "Very Strong"
        message = "Hurray! You have a very strong password."
    elif criteria_met == 4:
        strength = "Strong"
        message = "Hurray! You have a strong password."
    elif criteria_met == 3:
        strength = "Moderate"
        message = "Your password is moderate. Consider making it stronger."
    elif criteria_met == 2:
        strength = "Weak"
        message = "Oops! Your password is weak. Consider adding more complexity."
    else:
        strength = "Very Weak"
        message = "Oops! Your password is very weak. Consider adding more complexity."
        
    feedback = {
        "length_criteria": length_criteria,
        "upper_case_criteria": upper_case_criteria,
        "lower_case_criteria": lower_case_criteria,
        "number_criteria": number_criteria,
        "special_char_criteria": special_char_criteria,
        "strength": strength,
        "message": message
    }
    
    return feedback

# Example usage
password = getpass.getpass("Enter your password: ")
feedback = assess_password_strength(password)
print(f"Password Strength: {feedback['strength']}")
print(feedback['message'])
print("Criteria met:")
print(f" - Minimum length (8 characters): {'Yes' if feedback['length_criteria'] else 'No'}")
print(f" - Contains uppercase letters: {'Yes' if feedback['upper_case_criteria'] else 'No'}")
print(f" - Contains lowercase letters: {'Yes' if feedback['lower_case_criteria'] else 'No'}")
print(f" - Contains numbers: {'Yes' if feedback['number_criteria'] else 'No'}")
print(f" - Contains special characters: {'Yes' if feedback['special_char_criteria'] else 'No'}")
