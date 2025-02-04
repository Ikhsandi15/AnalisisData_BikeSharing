# Setup Environment

## Prerequisites
Pastikan Anda telah menginstal Python dan Git di komputer Anda. Jika belum, silakan instal terlebih dahulu.

## Clone Repository
Pertama, clone repositori proyek ke komputer lokal Anda menggunakan perintah berikut:

```bash
git clone https://github.com/Ikhsandi15/AnalisisData_BikeSharing.git
cd AnalisisData_BikeSharing
pip install pipenv
pipenv shell
pip install -r requirements.txt
streamlit run dashboard/dashboard.py
```