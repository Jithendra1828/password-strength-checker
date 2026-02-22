from password_utils import check_password_strength

def main():
    print("🔐 PASSWORD STRENGTH CHECKER 🔐")
    password = input("Enter your password: ")

    result = check_password_strength(password)

    print("\n--- Result ---")
    print(f"Strength: {result['strength']}")
    print(f"Score: {result['score']}/6")
    print(f"Security Percentage: {result['percentage']}%")

    if result['suggestions']:
        print("\nSuggestions to Improve:")
        for suggestion in result['suggestions']:
            print(f"- {suggestion}")
    else:
        print("\n✅ Excellent! Your password is secure.")

if __name__ == "__main__":
    main()
