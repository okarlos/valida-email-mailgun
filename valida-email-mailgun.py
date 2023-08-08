import requests

def valida_email(email):
    url = "https://api.mailgun.net/v4/address/validate"
    headers = {
        "Authorization": "ABC",  # Substitua pela sua chave API
    }
    params = {
        "address": email,
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()

def main():
    input_file = "lista_emails.txt"
    output_file = "resultados.txt"

    with open(input_file, "r") as f:
        emails = f.read().splitlines()

    with open(output_file, "w") as f_out:
        for email in emails:
            print(f"Validando e-mail: {email}")
            result = valida_email(email)
            result_value = result.get("result", "N/A")
            risk_value = result.get("risk", "N/A")
            result_line = f"{email};{result_value};{risk_value}"
            f_out.write(f"{result_line}\n")
            print(f"Result/Risk: {result_value}/{risk_value}")
            print("-" * 40)

    print(f"Resultados enviados para o arquivo {output_file}")

if __name__ == "__main__":
    main()
