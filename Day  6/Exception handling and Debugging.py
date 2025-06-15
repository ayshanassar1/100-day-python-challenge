def divide_numbers():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print("Result is:", result)
    
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")
    
    except ValueError:
        print("❌ Please enter valid numbers only!")
    
    except Exception as e:
        print("❌ An unexpected error occurred:", e)
    
    else:
        print("✅ Division successful!")
    
    finally:
        print("🔚 Operation complete.")

divide_numbers()

"""
Example Output 1:
Enter numerator: 10
Enter denominator: 2
Result is: 5.0
✅ Division successful!
🔚 Operation complete.

Example Output 2:
Enter numerator: 10
Enter denominator: 0
❌ Cannot divide by zero!
🔚 Operation complete.

Example Output 3:
Enter numerator: ten
❌ Please enter valid numbers only!
🔚 Operation complete.
"""

