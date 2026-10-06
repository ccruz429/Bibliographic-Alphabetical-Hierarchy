import re

def apa_alphabetize(references):
    """
    Organizes a list of APA 7th edition references alphabetically.

    Args:
        references: A list of strings, where each string is an APA reference.

    Returns:
        A new list of references, sorted alphabetically.
    """

    def extract_first_author(reference):
        """
        Extracts the first author's last name from an APA reference.
        Used for sorting.  Handles some common variations in author names.
        """
        match = re.search(r"([A-Z][a-z]+)\s(?:[A-Z][a-z]*\s)*,", reference) #find the first last name
        if match:
            return match.group(1)  # Return the first last name
        else:
            return ""  # Return an empty string if no last name is found

    # Sort the references using the extracted author's last name.
    sorted_references = sorted(references, key=extract_first_author)
    return sorted_references

def main():
    """
    Main function to demonstrate the alphabetization.
    """

    # Example References (replace with your actual references)
    references = [
"Alonso, M. (2026). SAFe: qué es y cómo aplicar esta metodología ágil a escala. Asana. https://asana.com/es/resources/safe-agile-at-scale",
"Wilmeth, R. (2024). Agile Release Train. Scaled Agile Framework. https://framework.scaledagile.com/agile-release-train",
"‌Wilmeth, R. (2024). PI Planning. Scaled Agile Framework. https://framework.scaledagile.com/pi-planning",
"‌Team Asana. (2026). VSM: qué es y cómo hacer un value stream mapping. Asana. https://asana.com/es/resources/value-stream-mapping"

    ]

    print("Unsorted References:")
    for reference in references:
        print(reference)

    sorted_references = apa_alphabetize(references)

    print("\nAlphabetized References:")
    for reference in sorted_references:
        print(reference)



if __name__ == "__main__":
    main()
