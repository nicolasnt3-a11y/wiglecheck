import tkinter as tk
from tkinter import messagebox
import requests
import re
from requests.auth import HTTPBasicAuth

# ---- CONFIGURATION ----
WIGLE_WIFI_URL = "https://api.wigle.net/api/v2/network/search"
WIGLE_BLUETOOTH_URL = "https://api.wigle.net/api/v2/bluetooth/search"

USERNAME = ""
PASSWORD = ""


def format_mac_address(mac):
    mac = re.sub(r"[^a-fA-F0-9]", "", mac)
    if len(mac) == 12:
        return ":".join(mac[i:i + 2] for i in range(0, 12, 2))
    return None


def search_mac(mac_address, result_text, network_type):
    mac_address = format_mac_address(mac_address)
    if not mac_address:
        messagebox.showerror("Erreur", "Adresse MAC invalide.")
        return

    url = WIGLE_WIFI_URL if network_type.get() == "wifi" else WIGLE_BLUETOOTH_URL
    params = {"netid": mac_address}

    try:
        response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), params=params)
        result_text.delete(1.0, tk.END)

        if response.headers.get("Content-Type", "").startswith("application/json"):
            data = response.json()

            if response.status_code == 200 and data.get("success"):
                if data.get("results"):
                    result = data["results"][0]
                    result_text.insert(tk.END, f"✅ Adresse MAC trouvée sur WiGLE ({network_type.get().capitalize()}) !\n")
                    result_text.insert(tk.END, f"📡 MAC : {result.get('netid', 'N/A')}\n")
                    result_text.insert(tk.END, f"📍 Latitude : {result.get('trilat', 'N/A')}\n")
                    result_text.insert(tk.END, f"📍 Longitude : {result.get('trilong', 'N/A')}\n")
                    if network_type.get() == "wifi":
                        result_text.insert(tk.END, f"🏠 SSID : {result.get('ssid', 'N/A')}\n")
                        result_text.insert(tk.END, f"📌 Rue : {result.get('road', 'N/A')}\n")
                        result_text.insert(tk.END, f"🏠 N° : {result.get('housenumber', 'N/A')}\n")
                        result_text.insert(tk.END, f"🏙 Ville : {result.get('city', 'N/A')}\n")
                        result_text.insert(tk.END, f"📮 CP : {result.get('postalcode', 'N/A')}\n")
                        result_text.insert(tk.END, f"🌍 Pays : {result.get('country', 'N/A')}\n")
                        result_text.insert(tk.END, f"🌍 Région : {result.get('region', 'N/A')}\n")
                    result_text.insert(tk.END, f"🕒 Première détection : {result.get('firsttime', 'N/A')}\n")
                    result_text.insert(tk.END, f"🕒 Dernière détection : {result.get('lasttime', 'N/A')}\n")
                else:
                    result_text.insert(tk.END, "❌ Aucune donnée trouvée pour cette adresse MAC.\n")
            else:
                result_text.insert(tk.END, f"❌ Erreur API ({response.status_code}) : {data.get('message', 'Erreur inconnue')}\n")
        else:
            result_text.insert(tk.END, "❌ Erreur : réponse non JSON.\n")
    except requests.exceptions.RequestException as e:
        result_text.insert(tk.END, f"❌ Erreur de connexion : {e}\n")


def create_gui():
    root = tk.Tk()
    root.title("Recherche d'adresse MAC sur WiGLE")
    root.geometry("520x450")

    label = tk.Label(root, text="Entrez une adresse MAC :")
    label.pack(pady=(10, 0))

    mac_entry = tk.Entry(root, width=50)
    mac_entry.insert(0, "ex: 00:11:22:33:44:55")
    mac_entry.pack(pady=5)

    network_type = tk.StringVar(value="wifi")
    radio_frame = tk.Frame(root)
    tk.Label(radio_frame, text="Type de réseau :").pack(side=tk.LEFT, padx=(0, 10))
    tk.Radiobutton(radio_frame, text="Wi-Fi", variable=network_type, value="wifi").pack(side=tk.LEFT)
    tk.Radiobutton(radio_frame, text="Bluetooth", variable=network_type, value="bluetooth").pack(side=tk.LEFT)
    radio_frame.pack(pady=10)

    result_text = tk.Text(root, width=65, height=15, wrap=tk.WORD)
    result_text.pack(pady=10)

    search_button = tk.Button(
        root,
        text="Rechercher",
        command=lambda: search_mac(mac_entry.get(), result_text, network_type)
    )
    search_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
