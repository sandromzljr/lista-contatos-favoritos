from typing import Dict, List

def add_contact(list: list) -> Dict:
    print("\n--------------------------------")
    name = input("Digite o nome do contato: ")
    phone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contact = {"name": name, "phone": phone, "email": email, "favorite": False}
    print("--------------------------------")
    list.append(contact)
    return

def list_contacts(list: list) -> None:
    for i, contact in enumerate(list):
        print("\n--------------------------------")
        print(f"CONTATO {i+1}")
        print("--------------------------------")
        print(f"Nome: {contact['name']}")
        print(f"Telefone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        is_favorite = "[ ★ ]" if contact["favorite"] else "[ ]"
        print(f"Favorito: {is_favorite}")
        print("--------------------------------")

def edit_contact(list: list) -> None:
    list_contacts(list)
    response_user = int(input("Digite o contato a ser alterado: "))
    if response_user >= 0 and response_user <= len(list):
        contact = list[response_user - 1]
        print(f"Contato {response_user}: {contact['name']}")
        name = input("Digite o novo nome do contato: ")
        phone = input("Digite o novo telefone do contato: ")
        email = input("Digite o novo email do contato: ")
        contact["name"] = name
        contact["phone"] = phone
        contact["email"] = email
        print(f"Contato {response_user} alterado com sucesso!")
        return
    else:
        print("Contato não encontrado!")
        return
    
def list_favorite_contacts(list: list) -> None:
    for i, contact in enumerate(list):
        if contact["favorite"]:
            print("\n--------------------------------")
            print(f"CONTATO {i+1}")
            print("--------------------------------")
            print(f"Nome: {contact['name']}")
            print(f"Telefone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            is_favorite = "[ ★ ]" if contact["favorite"] else "[ ]"
            print(f"Favorito: {is_favorite}")
            print("--------------------------------")
            return
        else:
            print("Você não possui nenhum contato favoritado!")

def check_favorite(list: list) -> None:
    list_contacts(list)
    response_user = int(input("Digite o contato a ser alterado: "))
    if response_user >= 0 and response_user <= len(list):
        contact = list[response_user - 1]
        contact["favorite"] = True
        return
    else:
        print("Contato não encontrado!")
        return
    
def delete_contact(list: list) -> None:
    list_contacts(list)
    response_user = int(input("Digite o contato a ser alterado: "))
    if response_user >= 0 and response_user <= len(list):
        contact = list[response_user - 1]
        name = contact["name"]
        list.remove(contact)
        print(f"Contato {name} apagado com sucesso!")
        return
    else:
        print("Contato não encontrado!")
        return

favorite_contacts = []
while True:
    print(f"""
/*****************************************************************\\
|           PROGRAMA PARA LISTAR SEUS CONTATOS FAVORITOS          |
|*****************************************************************|
| 1 - Criar Novo Contato                                          |
| 2 - Listar Contatos                                             |
| 3 - Editar Contato                                              |
| 4 - Marcar/Desmarcar Contato como Favorito                      |
| 5 - Listar Contatos Favoritos                                   |
| 6 - Apagar Contato                                              |
| 0 - Sair                                                        |
\*****************************************************************/""")
    user_response = int(input("\nDigite uma opção: "))

    match user_response:
        case 1:
            add_contact(favorite_contacts)
        case 2:
            list_contacts(favorite_contacts)
        case 3:
            edit_contact(favorite_contacts)
        case 4:
            check_favorite(favorite_contacts)
        case 5:
            list_favorite_contacts(favorite_contacts)
        case 6:
            delete_contact(favorite_contacts)
        case 0:
            print("\nSaindo...")
            break
        case _:
            print("Opção Inválida")