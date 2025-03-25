import datetime
import time
import os
import json
import random
import matplotlib.pyplot as plt
from colorama import init, Fore, Back, Style
from tabulate import tabulate
from tqdm import tqdm


# Inisialisasi colorama
init(autoreset=True)


class PerencanaanKarier:
    def __init__(self):
        self.tujuan_utama = []
        self.posisi_impian = ""
        self.keseimbangan_hidup = 0  # Skala 1-10
        self.anggaran_pendidikan = 0
        self.keterampilan_baru = []
        self.tingkat_keterampilan = {}
        self.kesempatan_kerja = []
        self.potensi_kesempatan = {}
        self.langkah_langkah = []
        self.prioritas_langkah = {}
        self.rencana_tahun = {}
        self.milestone_tahunan = {}
        self.risiko_tantangan = []
        self.strategi_mitigasi = {}
        self.jaringan_profesional = []
        self.tanggal_mulai = datetime.date.today()
        self.tanggal_target = self.tanggal_mulai.replace(year=self.tanggal_mulai.year + 5)
        self.profil_pengguna = {
            "nama": "",
            "usia": 0,
            "pendidikan_terakhir": "",
            "pengalaman_kerja": 0,
            "posisi_saat_ini": ""
        }
        self.status_pernikahan = ""
        self.jumlah_anak = 0
        self.kota_tinggal = ""
        self.preferensi_lokasi = []
        self.industri_target = []
        self.gaji_target = 0
        self.progres = 0  # Progres keseluruhan rencana karier


    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
   
    def animation_loading(self, text):
        for i in range(3):
            print(f"\r{text}" + "." * (i + 1) + " " * (3 - i), end="")
            time.sleep(0.3)
        print()
   
    def display_header(self, title):
        self.clear_screen()
        print(f"\n{Fore.CYAN}{Style.BRIGHT}" + "=" * 70)
        print(f"{Fore.YELLOW}{Style.BRIGHT}{title:^70}")
        print(f"{Fore.CYAN}{Style.BRIGHT}" + "=" * 70 + "\n")
   
    def input_profil(self):
        self.display_header("PROFIL PENGGUNA")
        print(f"{Fore.GREEN}Silakan masukkan informasi profil Anda untuk membuat rencana yang lebih personal.")
       
        self.profil_pengguna["nama"] = input(f"{Fore.WHITE}Nama Lengkap: ")
       
        while True:
            try:
                self.profil_pengguna["usia"] = int(input(f"{Fore.WHITE}Usia: "))
                if 15 <= self.profil_pengguna["usia"] <= 65:
                    break
                else:
                    print(f"{Fore.RED}Masukkan usia yang valid (15-65 tahun).")
            except ValueError:
                print(f"{Fore.RED}Masukkan angka yang valid.")
       
        self.profil_pengguna["pendidikan_terakhir"] = input(f"{Fore.WHITE}Pendidikan Terakhir: ")
       
        while True:
            try:
                self.profil_pengguna["pengalaman_kerja"] = float(input(f"{Fore.WHITE}Pengalaman Kerja (dalam tahun): "))
                if self.profil_pengguna["pengalaman_kerja"] >= 0:
                    break
                else:
                    print(f"{Fore.RED}Pengalaman kerja tidak boleh negatif.")
            except ValueError:
                print(f"{Fore.RED}Masukkan angka yang valid.")
       
        self.profil_pengguna["posisi_saat_ini"] = input(f"{Fore.WHITE}Posisi Saat Ini: ")
        self.status_pernikahan = input(f"{Fore.WHITE}Status Pernikahan: ")
       
        if self.status_pernikahan.lower() in ["menikah", "married"]:
            while True:
                try:
                    self.jumlah_anak = int(input(f"{Fore.WHITE}Jumlah Anak: "))
                    if self.jumlah_anak >= 0:
                        break
                    else:
                        print(f"{Fore.RED}Jumlah anak tidak boleh negatif.")
                except ValueError:
                    print(f"{Fore.RED}Masukkan angka yang valid.")
       
        self.kota_tinggal = input(f"{Fore.WHITE}Kota Tinggal Saat Ini: ")
       
        print(f"\n{Fore.GREEN}Preferensi Lokasi Kerja (masukkan 'selesai' jika sudah selesai):")
        while True:
            lokasi = input(f"{Fore.WHITE}Lokasi: ")
            if lokasi.lower() == 'selesai':
                break
            self.preferensi_lokasi.append(lokasi)
       
        print(f"\n{Fore.GREEN}Industri Target (masukkan 'selesai' jika sudah selesai):")
        while True:
            industri = input(f"{Fore.WHITE}Industri: ")
            if industri.lower() == 'selesai':
                break
            self.industri_target.append(industri)
       
        while True:
            try:
                self.gaji_target = int(input(f"{Fore.WHITE}Gaji Target dalam 5 Tahun (dalam juta rupiah): "))
                if self.gaji_target >= 0:
                    break
                else:
                    print(f"{Fore.RED}Gaji target tidak boleh negatif.")
            except ValueError:
                print(f"{Fore.RED}Masukkan angka yang valid.")
       
        print(f"\n{Fore.GREEN}Profil pengguna berhasil disimpan!")
        time.sleep(1)
   
    def tentukan_posisi_impian(self):
        self.display_header("LANGKAH 1: MENENTUKAN POSISI IMPIAN")
       
        print(f"{Fore.GREEN}Contoh posisi: manajer proyek, insinyur senior, pengusaha, dll.")
        self.posisi_impian = input(f"{Fore.WHITE}Masukkan posisi atau profesi impian Anda: ")
       
        print(f"\n{Fore.GREEN}Tujuan Utama (masukkan 'selesai' jika sudah selesai):")
        print(f"{Fore.YELLOW}Tips: Pikirkan tentang motivasi, nilai, dan aspirasi Anda.")
       
        while True:
            tujuan = input(f"{Fore.WHITE}Tujuan: ")
            if tujuan.lower() == 'selesai':
                break
            self.tujuan_utama.append(tujuan)
       
        print(f"\n{Fore.GREEN}Posisi impian dan tujuan utama berhasil disimpan!")
        time.sleep(1)


    def tentukan_keseimbangan_hidup(self):
        self.display_header("LANGKAH 2: KESEIMBANGAN HIDUP-KERJA")
    
        print(f"{Fore.GREEN}Tentukan keseimbangan hidup-kerja yang ideal untuk Anda.")
        print(f"{Fore.YELLOW}Skala 0-10 (0 = fokus pada kerja, 10 = fokus pada hidup pribadi)")
    
        while True:
            try:
                self.keseimbangan_hidup = int(input(f"{Fore.WHITE}Tentukan target keseimbangan hidup-kerja (skala 0-10): "))
                if 0 <= self.keseimbangan_hidup <= 10:
                    break
                else:
                    print(f"{Fore.RED}Masukkan angka antara 0 sampai 10.")
            except ValueError:
                print(f"{Fore.RED}Masukkan angka yang valid.")
    
    # Visualisasi
        print(f"\n{Fore.CYAN}Visualisasi Keseimbangan Hidup-Kerja:")
        total_chars = 40
    
    # Hitung persentase
        work_percent = (10 - self.keseimbangan_hidup) * 10  # 0-100%
        life_percent = self.keseimbangan_hidup * 10
    
    # Hitung panjang bar
        work_chars = int(work_percent / 100 * total_chars)
        life_chars = total_chars - work_chars
    
    # Bar warna
        work_bar = Back.BLUE + ' ' * work_chars + Style.RESET_ALL
        life_bar = Back.GREEN + ' ' * life_chars + Style.RESET_ALL
    
    # Tampilkan bar
        print(f"{Fore.BLUE}Kerja{Fore.WHITE}|{work_bar}{life_bar}|{Fore.GREEN}Hidup Pribadi")
    
    # Tampilkan persentase di tengah bar
        work_text = f"Kerja: {work_percent}%"
        life_text = f"Hidup Pribadi: {life_percent}%"
    
    # Hitung posisi tengah untuk masing-masing teks persentase
        work_position = work_chars // 2 - len(work_text) // 2
        life_position = work_chars + (life_chars // 2) - len(life_text) // 2
    
    # Buat spasi untuk posisi teks
        work_spaces = " " * max(0, work_position)
        life_spaces = " " * max(0, (life_position - len(work_text) - work_position))
    
    # Tampilkan persentase di tengah
        print(f"\n{Fore.WHITE}{work_spaces}{work_text}{life_spaces}{life_text}")
    
        print(f"\n{Fore.GREEN}Keseimbangan hidup-kerja berhasil disimpan!")
        time.sleep(1)
   
    def tentukan_anggaran(self):
        self.display_header("LANGKAH 3: ANGGARAN PENGEMBANGAN DIRI")
       
        print(f"{Fore.GREEN}Tentukan anggaran untuk pengembangan diri Anda.")
        print(f"{Fore.YELLOW}Tips: Pertimbangkan biaya kursus, sertifikasi, pelatihan, dan alat-alat kerja.")
       
        while True:
            try:
                self.anggaran_pendidikan = int(input(f"{Fore.WHITE}Masukkan anggaran untuk pendidikan/pelatihan per tahun (dalam ribu rupiah): "))
                if self.anggaran_pendidikan >= 0:
                    break
                else:
                    print(f"{Fore.RED}Anggaran tidak boleh negatif.")
            except ValueError:
                print(f"{Fore.RED}Masukkan angka yang valid.")
       
        print(f"\n{Fore.GREEN}Anggaran pengembangan diri berhasil disimpan!")
        time.sleep(1)
   
    def identifikasi_keterampilan(self):
        self.display_header("LANGKAH 4: IDENTIFIKASI KETERAMPILAN YANG DIPERLUKAN")
       
        print(f"{Fore.GREEN}Identifikasi keterampilan yang diperlukan untuk posisi impian Anda.")
        print(f"{Fore.YELLOW}Tips: Peneliti posisi karier impian, lihat lowongan kerja, atau tanyakan pada profesional.")
        print(f"{Fore.YELLOW}Masukkan keterampilan satu per satu. Ketik 'selesai' jika sudah selesai.")
       
        while True:
            keterampilan = input(f"{Fore.WHITE}Masukkan keterampilan yang ingin dikembangkan (atau 'selesai'): ")
            if keterampilan.lower() == 'selesai':
                break
           
            while True:
                try:
                    tingkat = int(input(f"{Fore.WHITE}Tingkat keterampilan saat ini (1-10): "))
                    if 1 <= tingkat <= 10:
                        self.keterampilan_baru.append(keterampilan)
                        self.tingkat_keterampilan[keterampilan] = tingkat
                        break
                    else:
                        print(f"{Fore.RED}Masukkan angka antara 1 sampai 10.")
                except ValueError:
                    print(f"{Fore.RED}Masukkan angka yang valid.")
       
        # Tampilkan keterampilan dengan gradient berdasarkan level
        if self.keterampilan_baru:
            print(f"\n{Fore.CYAN}Keterampilan dan Tingkat Saat Ini:")
            max_name_length = max(len(skill) for skill in self.keterampilan_baru)
           
            for skill in self.keterampilan_baru:
                level = self.tingkat_keterampilan[skill]
                progress_bar = ""
               
                # Tentukan warna berdasarkan level keterampilan
                for i in range(10):
                    if i < level:  # Bagian yang terisi
                        if i < 3:
                            progress_bar += Fore.RED + "█"
                        elif i < 7:  
                            progress_bar += Fore.YELLOW + "█"
                        else:
                            progress_bar += Fore.LIGHTGREEN_EX + "█"
                    else:  # Bagian yang belum terisi
                        progress_bar += Fore.WHITE + "░"
               
                # Tentukan warna angka level berdasarkan tingkat
                level_color = Fore.RED if level <= 4 else (Fore.YELLOW if level <= 7 else Fore.GREEN)
               
                print(
                    f"{Fore.WHITE}{skill[:20]:<{max_name_length}} : "
                    f"{progress_bar} {level_color}{level}/10"
                )
       
        print(f"\n{Fore.GREEN}Keterampilan berhasil disimpan!")
        time.sleep(1)
   
    def analisis_kesempatan(self):
        self.display_header("LANGKAH 5: ANALISIS KESEMPATAN KERJA")
       
        print(f"{Fore.GREEN}Identifikasi kesempatan kerja yang tersedia di pasar.")
        print(f"{Fore.YELLOW}Tips: Cari informasi tren industri, pertumbuhan posisi, dan gaji.")
        print(f"{Fore.YELLOW}Masukkan kesempatan satu per satu. Ketik 'selesai' jika sudah selesai.")
       
        while True:
            kesempatan = input(f"{Fore.WHITE}Masukkan kesempatan kerja yang tersedia (atau 'selesai'): ")
            if kesempatan.lower() == 'selesai':
                break
           
            while True:
                try:
                    potensi = int(input(f"{Fore.WHITE}Potensi kesempatan (1-10): "))
                    if 1 <= potensi <= 10:
                        self.kesempatan_kerja.append(kesempatan)
                        self.potensi_kesempatan[kesempatan] = potensi
                        break
                    else:
                        print(f"{Fore.RED}Masukkan angka antara 1 sampai 10.")
                except ValueError:
                    print(f"{Fore.RED}Masukkan angka yang valid.")
       
        # Tampilkan kesempatan dan potensinya
        if self.kesempatan_kerja:
            print(f"\n{Fore.CYAN}Kesempatan Kerja dan Potensinya:")
            for opp in self.kesempatan_kerja:
                potential = self.potensi_kesempatan[opp]
                print(f"{Fore.WHITE}{opp}: {Fore.YELLOW}{potential}/10 {Fore.GREEN}{'★' * potential}{Fore.WHITE}{'☆' * (10 - potential)}")
       
        print(f"\n{Fore.GREEN}Kesempatan kerja berhasil disimpan!")
        time.sleep(1)
   
    def tentukan_langkah_langkah(self):
        self.display_header("LANGKAH 6: TENTUKAN LANGKAH-LANGKAH POTENSIAL")
       
        print(f"{Fore.GREEN}Tentukan langkah-langkah potensial untuk mencapai tujuan Anda.")
        print(f"{Fore.YELLOW}Contoh: Melanjutkan studi (S2), mengambil posisi junior, bergabung dengan organisasi profesional.")
        print(f"{Fore.YELLOW}Masukkan langkah-langkah satu per satu. Ketik 'selesai' jika sudah selesai.")
       
        while True:
            langkah = input(f"{Fore.WHITE}Masukkan langkah potensial (atau 'selesai'): ")
            if langkah.lower() == 'selesai':
                break
           
            while True:
                try:
                    prioritas = int(input(f"{Fore.WHITE}Prioritas langkah ini (1-5, 1=tertinggi): "))
                    if 1 <= prioritas <= 5:
                        self.langkah_langkah.append(langkah)
                        self.prioritas_langkah[langkah] = prioritas
                        break
                    else:
                        print(f"{Fore.RED}Masukkan angka antara 1 sampai 5.")
                except ValueError:
                    print(f"{Fore.RED}Masukkan angka yang valid.")
       
        # Tampilkan langkah-langkah dan prioritasnya
        if self.langkah_langkah:
            print(f"\n{Fore.CYAN}Langkah-langkah Potensial dan Prioritasnya:")
           
            # Urutkan langkah-langkah berdasarkan prioritas
            langkah_sorted = sorted(self.langkah_langkah, key=lambda x: self.prioritas_langkah[x])
           
            for step in langkah_sorted:
                priority = self.prioritas_langkah[step]
                print(f"{Fore.WHITE}[{priority}] {step}")
       
        print(f"\n{Fore.GREEN}Langkah-langkah potensial berhasil disimpan!")
        time.sleep(1)
   
    def identifikasi_risiko(self):
        self.display_header("LANGKAH 7: IDENTIFIKASI RISIKO & TANTANGAN")
       
        print(f"{Fore.GREEN}Identifikasi risiko dan tantangan yang mungkin Anda hadapi.")
        print(f"{Fore.YELLOW}Tips: Pikirkan tentang hambatan, persaingan, dan faktor eksternal lainnya.")
        print(f"{Fore.YELLOW}Masukkan risiko satu per satu. Ketik 'selesai' jika sudah selesai.")
       
        while True:
            risiko = input(f"{Fore.WHITE}Masukkan risiko atau tantangan (atau 'selesai'): ")
            if risiko.lower() == 'selesai':
                break
           
            mitigasi = input(f"{Fore.WHITE}Strategi mitigasi untuk risiko ini: ")
            self.risiko_tantangan.append(risiko)
            self.strategi_mitigasi[risiko] = mitigasi
       
        # Tampilkan risiko dan strateginya
        if self.risiko_tantangan:
            print(f"\n{Fore.CYAN}Risiko dan Strategi Mitigasi:")
           
            table_data = []
            for risk in self.risiko_tantangan:
                table_data.append([risk, self.strategi_mitigasi[risk]])
           
            headers = ["Risiko/Tantangan", "Strategi Mitigasi"]
            print(tabulate(table_data, headers=headers, tablefmt="pretty"))
       
        print(f"\n{Fore.GREEN}Risiko dan strategi mitigasi berhasil disimpan!")
        time.sleep(1)
   
    def jaringan_profesional_input(self):
        self.display_header("LANGKAH 8: JARINGAN PROFESIONAL")
       
        print(f"{Fore.GREEN}Identifikasi jaringan profesional yang dapat membantu karier Anda.")
        print(f"{Fore.YELLOW}Tips: Pikirkan tentang mentor, komunitas profesional, dan konferensi.")
        print(f"{Fore.YELLOW}Masukkan jaringan satu per satu. Ketik 'selesai' jika sudah selesai.")
       
        while True:
            jaringan = input(f"{Fore.WHITE}Masukkan jaringan profesional (atau 'selesai'): ")
            if jaringan.lower() == 'selesai':
                break
            self.jaringan_profesional.append(jaringan)
       
        # Tampilkan jaringan profesional
        if self.jaringan_profesional:
            print(f"\n{Fore.CYAN}Jaringan Profesional:")
            for i, network in enumerate(self.jaringan_profesional, 1):
                print(f"{Fore.WHITE}{i}. {network}")
       
        print(f"\n{Fore.GREEN}Jaringan profesional berhasil disimpan!")
        time.sleep(1)
   
    def susun_rencana_tahunan(self):
        self.display_header("LANGKAH 9: SUSUN RENCANA TAHUNAN")
       
        print(f"{Fore.GREEN}Susun rencana tahunan untuk 5 tahun ke depan.")
        print(f"{Fore.YELLOW}Tips: Tentukan tujuan, aktivitas, dan milestone spesifik untuk setiap tahun.")
       
        for tahun in range(1, 6):
            print(f"\n{Fore.CYAN}RENCANA TAHUN {tahun}:")
           
            rencana = input(f"{Fore.WHITE}Masukkan rencana untuk tahun ke-{tahun}: ")
            target = input(f"{Fore.WHITE}Masukkan target yang ingin dicapai: ")
            aktivitas = input(f"{Fore.WHITE}Aktivitas utama yang akan dilakukan: ")
            evaluasi = input(f"{Fore.WHITE}Bagaimana Anda akan mengevaluasi kemajuan: ")
           
            print(f"{Fore.YELLOW}Milestone untuk tahun ke-{tahun} (masukkan 'selesai' jika sudah selesai):")
            milestones = []
            while True:
                milestone = input(f"{Fore.WHITE}Milestone: ")
                if milestone.lower() == 'selesai':
                    break
                milestones.append(milestone)
           
            self.rencana_tahun[tahun] = {
                "rencana": rencana,
                "target": target,
                "aktivitas": aktivitas,
                "evaluasi": evaluasi
            }
           
            self.milestone_tahunan[tahun] = milestones
           
            print(f"{Fore.GREEN}Rencana tahun ke-{tahun} berhasil disimpan!")
            time.sleep(0.5)
       
        print(f"\n{Fore.GREEN}Seluruh rencana tahunan berhasil disimpan!")
        time.sleep(1)
   
    def visualisasi_rencana(self):
        self.display_header("VISUALISASI RENCANA KARIER")
       
        # Visualisasi Keterampilan
        if self.keterampilan_baru:
            print(f"\n{Fore.CYAN}Grafik Keterampilan:")
           
            skills = self.keterampilan_baru[:5]  # Ambil 5 keterampilan pertama
            levels = [self.tingkat_keterampilan[skill] for skill in skills]
           
            # Buat bar chart sederhana
            for i, skill in enumerate(skills):
                level = levels[i]
                print(f"{Fore.WHITE}{skill[:15]:<15}: {Fore.GREEN}{'█' * level}{Fore.WHITE}{'█' * (10 - level)} {level}/10")
       
        # Visualisasi Prioritas Langkah
        if self.langkah_langkah:
            print(f"\n{Fore.CYAN}Prioritas Langkah:")
           
            # Urutkan langkah-langkah berdasarkan prioritas
            langkah_sorted = sorted(self.langkah_langkah, key=lambda x: self.prioritas_langkah[x])
           
            for step in langkah_sorted:
                priority = self.prioritas_langkah[step]
                stars = '★' * (6 - priority)
                print(f"{Fore.WHITE}{step[:30]:<30}: {Fore.YELLOW}{stars}")
       
        # Visualisasi Timeline Rencana
        print(f"\n{Fore.CYAN}Timeline Rencana:")
        print(f"{Fore.WHITE}{'Tahun 1':^14}{'Tahun 2':^14}{'Tahun 3':^14}{'Tahun 4':^14}{'Tahun 5':^14}")
        print(f"{Fore.WHITE}{'▼':^14}{'▼':^14}{'▼':^14}{'▼':^14}{'▼':^14}")
        print(f"{Fore.GREEN}{'═══════════':<14}{'═══════════':<14}{'═══════════':<14}{'═══════════':<14}{'═══════════':<14}")
       
        # Tampilkan milestone untuk setiap tahun
        max_milestones = max([len(ms) for ms in self.milestone_tahunan.values()]) if self.milestone_tahunan else 0
       
        for i in range(max_milestones):
            line = ""
            for tahun in range(1, 6):
                if tahun in self.milestone_tahunan and i < len(self.milestone_tahunan[tahun]):
                    milestone = self.milestone_tahunan[tahun][i]
                    line += f"{Fore.WHITE}• {milestone[:10]:<12}"
                else:
                    line += f"{Fore.WHITE}{' ':^14}"
            print(line)
       
        print(f"\n{Fore.GREEN}Visualisasi rencana selesai!")
        time.sleep(5)
   
    def tampilkan_ringkasan(self):


        if not self.profil_pengguna["nama"] or not self.posisi_impian:
            print(f"{Fore.RED}Belum ada data rencana karier. Silakan buat rencana baru atau muat dari file terlebih dahulu.")
            time.sleep(2)
            return


        self.display_header("RINGKASAN RENCANA KARIER 5 TAHUN")
       
        print(f"{Fore.CYAN}Profil Pengguna:")
        print(f"{Fore.WHITE}Nama: {self.profil_pengguna['nama']}")
        print(f"{Fore.WHITE}Usia: {self.profil_pengguna['usia']} tahun")
        print(f"{Fore.WHITE}Pendidikan Terakhir: {self.profil_pengguna['pendidikan_terakhir']}")
        print(f"{Fore.WHITE}Pengalaman Kerja: {self.profil_pengguna['pengalaman_kerja']} tahun")
        print(f"{Fore.WHITE}Posisi Saat Ini: {self.profil_pengguna['posisi_saat_ini']}")
       
        print(f"\n{Fore.CYAN}Informasi Rencana:")
        print(f"{Fore.WHITE}Tanggal Mulai: {self.tanggal_mulai.strftime('%d-%m-%Y')}")
        print(f"{Fore.WHITE}Tanggal Target: {self.tanggal_target.strftime('%d-%m-%Y')}")
        print(f"{Fore.WHITE}Posisi Impian: {self.posisi_impian}")
        print(f"{Fore.WHITE}Target Keseimbangan Hidup-Kerja: {self.keseimbangan_hidup}/10")
        print(f"{Fore.WHITE}Anggaran Pengembangan Diri: Rp {self.anggaran_pendidikan:,} per tahun")
        print(f"{Fore.WHITE}Gaji Target dalam 5 Tahun: Rp {self.gaji_target:,} juta")
       
        if self.tujuan_utama:
            print(f"\n{Fore.CYAN}Tujuan Utama:")
            for i, tujuan in enumerate(self.tujuan_utama, 1):
                print(f"{Fore.WHITE}{i}. {tujuan}")
       
        if self.keterampilan_baru:
            print(f"\n{Fore.CYAN}Keterampilan yang Perlu Dikembangkan:")
            data = []
            for keterampilan in self.keterampilan_baru:
                data.append([keterampilan, f"{self.tingkat_keterampilan[keterampilan]}/10"])
            print(tabulate(data, headers=["Keterampilan", "Tingkat Saat Ini"], tablefmt="pretty"))
       
        if self.kesempatan_kerja:
            print(f"\n{Fore.CYAN}Kesempatan Kerja yang Diidentifikasi:")
            data = []
            for kesempatan in self.kesempatan_kerja:
                data.append([kesempatan, f"{self.potensi_kesempatan[kesempatan]}/10"])
            print(tabulate(data, headers=["Kesempatan", "Potensi"], tablefmt="pretty"))
       
        if self.langkah_langkah:
            print(f"\n{Fore.CYAN}Langkah-langkah Potensial:")
            data = []
            for langkah in sorted(self.langkah_langkah, key=lambda x: self.prioritas_langkah[x]):
                data.append([langkah, f"Prioritas {self.prioritas_langkah[langkah]}/5"])
            print(tabulate(data, headers=["Langkah", "Prioritas"], tablefmt="pretty"))
       
        if self.risiko_tantangan:
            print(f"\n{Fore.CYAN}Risiko dan Strategi Mitigasi:")
            data = []
            for risiko in self.risiko_tantangan:
                data.append([risiko, self.strategi_mitigasi[risiko]])
            print(tabulate(data, headers=["Risiko/Tantangan", "Strategi Mitigasi"], tablefmt="pretty"))
       
        if self.jaringan_profesional:
            print(f"\n{Fore.CYAN}Jaringan Profesional:")
            for i, jaringan in enumerate(self.jaringan_profesional, 1):
                print(f"{Fore.WHITE}{i}. {jaringan}")
       
        print(f"\n{Fore.CYAN}Rencana Tahunan:")
        for tahun, detail in self.rencana_tahun.items():
            print(f"\n{Fore.YELLOW}Tahun {tahun}:")
            print(f"{Fore.WHITE}  Rencana: {detail['rencana']}")
            print(f"{Fore.WHITE}  Target: {detail['target']}")
            print(f"{Fore.WHITE}  Aktivitas: {detail['aktivitas']}")
            print(f"{Fore.WHITE}  Evaluasi: {detail['evaluasi']}")
           
            if self.milestone_tahunan[tahun]:
                print(f"{Fore.WHITE}  Milestone:")
                for i, milestone in enumerate(self.milestone_tahunan[tahun], 1):
                    print(f"{Fore.WHITE}    {i}. {milestone}")
   
    def simpan_ke_file(self):
        self.display_header("SIMPAN RENCANA KARIER")
       
        print(f"{Fore.GREEN}Menyimpan rencana karier ke file...")
       
        # Simpan sebagai JSON
        data = {
            "profil_pengguna": self.profil_pengguna,
            "tanggal_mulai": self.tanggal_mulai.strftime('%Y-%m-%d'),
            "tanggal_target": self.tanggal_target.strftime('%Y-%m-%d'),
            "posisi_impian": self.posisi_impian,
            "tujuan_utama": self.tujuan_utama,
            "keseimbangan_hidup": self.keseimbangan_hidup,
            "anggaran_pendidikan": self.anggaran_pendidikan,
            "keterampilan_baru": self.keterampilan_baru,
            "tingkat_keterampilan": self.tingkat_keterampilan,
            "kesempatan_kerja": self.kesempatan_kerja,
            "potensi_kesempatan": self.potensi_kesempatan,
            "langkah_langkah": self.langkah_langkah,
            "prioritas_langkah": self.prioritas_langkah,
            "rencana_tahun": self.rencana_tahun,
            "milestone_tahunan": self.milestone_tahunan,
            "risiko_tantangan": self.risiko_tantangan,
            "strategi_mitigasi": self.strategi_mitigasi,
            "jaringan_profesional": self.jaringan_profesional,
            "status_pernikahan": self.status_pernikahan,
            "jumlah_anak": self.jumlah_anak,
            "kota_tinggal": self.kota_tinggal,
            "preferensi_lokasi": self.preferensi_lokasi,
            "industri_target": self.industri_target,
            "gaji_target": self.gaji_target,
            "progres": self.progres
        }
       
        # Tentukan nama file
        nama_file = f"rencana_karier_{self.profil_pengguna['nama'].replace(' ', '_')}.json"
       
        # Simpan ke file
        with open(nama_file, 'w') as file:
            json.dump(data, file, indent=4)
       
        print(f"\n{Fore.GREEN}Rencana karier berhasil disimpan ke file {nama_file}!")
        time.sleep(5)
   
    def muat_dari_file(self):
        self.display_header("MUAT RENCANA KARIER DARI FILE")
       
        print(f"{Fore.GREEN}Masukkan nama file rencana karier yang ingin dimuat:")
        nama_file = input(f"{Fore.WHITE}Nama File: ")
       
        try:
            with open(nama_file, 'r') as file:
                data = json.load(file)
           
            # Muat data ke atribut kelas
            self.profil_pengguna = data["profil_pengguna"]
            self.tanggal_mulai = datetime.datetime.strptime(data["tanggal_mulai"], '%Y-%m-%d').date()
            self.tanggal_target = datetime.datetime.strptime(data["tanggal_target"], '%Y-%m-%d').date()
            self.posisi_impian = data["posisi_impian"]
            self.tujuan_utama = data["tujuan_utama"]
            self.keseimbangan_hidup = data["keseimbangan_hidup"]
            self.anggaran_pendidikan = data["anggaran_pendidikan"]
            self.keterampilan_baru = data["keterampilan_baru"]
            self.tingkat_keterampilan = data["tingkat_keterampilan"]
            self.kesempatan_kerja = data["kesempatan_kerja"]
            self.potensi_kesempatan = data["potensi_kesempatan"]
            self.langkah_langkah = data["langkah_langkah"]
            self.prioritas_langkah = data["prioritas_langkah"]
            self.rencana_tahun = data["rencana_tahun"]
            self.milestone_tahunan = data["milestone_tahunan"]
            self.risiko_tantangan = data["risiko_tantangan"]
            self.strategi_mitigasi = data["strategi_mitigasi"]
            self.jaringan_profesional = data["jaringan_profesional"]
            self.status_pernikahan = data["status_pernikahan"]
            self.jumlah_anak = data["jumlah_anak"]
            self.kota_tinggal = data["kota_tinggal"]
            self.preferensi_lokasi = data["preferensi_lokasi"]
            self.industri_target = data["industri_target"]
            self.gaji_target = data["gaji_target"]
            self.progres = data["progres"]
           
            print(f"\n{Fore.GREEN}Rencana karier berhasil dimuat dari file {nama_file}!")
            time.sleep(5)
       
        except FileNotFoundError:
            print(f"\n{Fore.RED}File tidak ditemukan!")
            time.sleep(1)
        except json.JSONDecodeError:
            print(f"\n{Fore.RED}File tidak valid atau rusak!")
            time.sleep(1)
   
    def hitung_progres(self):
        total_langkah = len(self.langkah_langkah)
        if total_langkah == 0:
            return 0
       
        langkah_selesai = 0
        for langkah in self.langkah_langkah:
            if self.prioritas_langkah[langkah] == 1:  # Prioritas tertinggi
                langkah_selesai += 1
       
        self.progres = (langkah_selesai / total_langkah) * 100
        return self.progres
   
    def tampilkan_progres(self):
        self.display_header("PROGRES RENCANA KARIER")
       
        print(f"{Fore.CYAN}Progres Keseluruhan: {self.hitung_progres():.2f}%")
       
        if self.langkah_langkah:
            print(f"\n{Fore.CYAN}Langkah-langkah yang Sudah Dikerjakan:")
            for langkah in self.langkah_langkah:
                if self.prioritas_langkah[langkah] == 1:
                    print(f"{Fore.WHITE}✓ {langkah}")
       
        print(f"\n{Fore.CYAN}Langkah-langkah yang Belum Dikerjakan:")
        for langkah in self.langkah_langkah:
            if self.prioritas_langkah[langkah] != 1:
                print(f"{Fore.WHITE}✗ {langkah}")
       
        print(f"\n{Fore.GREEN}Progres rencana karier berhasil ditampilkan!")
        time.sleep(5)
   
    def menu_utama(self):
        while True:
            self.display_header("MENU UTAMA")
           
            print(f"{Fore.CYAN}1. Buat Rencana Karier Baru")
            print(f"{Fore.CYAN}2. Muat Rencana Karier dari File")
            print(f"{Fore.CYAN}3. Tampilkan Ringkasan Rencana")
            print(f"{Fore.CYAN}4. Visualisasi Rencana")
            print(f"{Fore.CYAN}5. Tampilkan Progres")
            print(f"{Fore.CYAN}6. Simpan Rencana ke File")
            print(f"{Fore.CYAN}7. Edit Rencana")  # Menu baru
            print(f"{Fore.CYAN}8. Keluar")  # Keluar pindah ke 8

            pilihan = input(f"\n{Fore.WHITE}Pilih menu (1-8): ")
           
            if pilihan == '1':
                self.input_profil()
                self.tentukan_posisi_impian()
                self.tentukan_keseimbangan_hidup()
                self.tentukan_anggaran()
                self.identifikasi_keterampilan()
                self.analisis_kesempatan()
                self.tentukan_langkah_langkah()
                self.identifikasi_risiko()
                self.jaringan_profesional_input()
                self.susun_rencana_tahunan()
            elif pilihan == '2':
                self.muat_dari_file()
            elif pilihan == '3':
                self.tampilkan_ringkasan()
            elif pilihan == '4':
                self.visualisasi_rencana()
            elif pilihan == '5':
                self.tampilkan_progres()
            elif pilihan == '6':
                self.simpan_ke_file()
            elif pilihan == '7':  # Menu edit baru
                self.menu_edit()
            elif pilihan == '8':  # Keluar pindah ke sini
                print(f"\n{Fore.GREEN}Terima kasih telah menggunakan aplikasi ini!")
                break
            else:
                print(f"\n{Fore.RED}Pilihan tidak valid. Silakan coba lagi.")
                time.sleep(1)
    def menu_edit(self):
        if not self.profil_pengguna["nama"]:
            print(f"{Fore.RED}Belum ada data rencana. Silakan buat atau muat rencana terlebih dahulu.")
            time.sleep(2)
            return

        while True:
            self.display_header("EDIT RENCANA KARIER")
            print(f"{Fore.CYAN}1. Edit Profil Pengguna")
            print(f"{Fore.CYAN}2. Edit Posisi Impian & Tujuan")
            print(f"{Fore.CYAN}3. Edit Keseimbangan Hidup-Kerja")
            print(f"{Fore.CYAN}4. Edit Anggaran Pendidikan")
            print(f"{Fore.CYAN}5. Edit Keterampilan")
            print(f"{Fore.CYAN}6. Edit Analisis Kesempatan Kerja")
            print(f"{Fore.CYAN}7. Edit Langkah-langkah")
            print(f"{Fore.CYAN}8. Edit Risiko & Mitigasi")
            print(f"{Fore.CYAN}9. Edit Jaringan Profesional")
            print(f"{Fore.CYAN}10. Edit Rencana Tahunan")
            print(f"{Fore.CYAN}11. Kembali ke Menu Utama")

            pilihan = input(f"\n{Fore.WHITE}Pilih bagian yang ingin diedit (1-11): ")

            if pilihan == '1':
                self.edit_profil()
            elif pilihan == '2':
                self.tentukan_posisi_impian()
            elif pilihan == '3':
                self.tentukan_keseimbangan_hidup()
            elif pilihan == '4':
                self.tentukan_anggaran()
            elif pilihan == '5':
                self.identifikasi_keterampilan()
            elif pilihan == '6':
                self.analisis_kesempatan()
            elif pilihan == '7':
                self.tentukan_langkah_langkah()
            elif pilihan == '8':
                self.identifikasi_risiko()
            elif pilihan == '9':
                self.jaringan_profesional_input()
            elif pilihan == '10':
                self.edit_rencana_tahunan()
            elif pilihan == '11':
                break
            else:
                print(f"{Fore.RED}Pilihan tidak valid!")
                time.sleep(1)
    def edit_rencana_tahunan(self):
        self.display_header("EDIT RENCANA TAHUNAN")
        
        # Pilih tahun yang akan diedit
        while True:
            try:
                tahun = int(input(f"{Fore.WHITE}Masukkan tahun yang ingin diedit (1-5): "))
                if 1 <= tahun <= 5:
                    break
                else:
                    print(f"{Fore.RED}Masukkan tahun antara 1-5!")
            except ValueError:
                print(f"{Fore.RED}Masukkan angka yang valid!")

        # Tampilkan data existing jika ada
        if tahun in self.rencana_tahun:
            print(f"\n{Fore.YELLOW}Rencana Saat Ini untuk Tahun {tahun}:")
            print(f"{Fore.WHITE}Rencana: {self.rencana_tahun[tahun]['rencana']}")
            print(f"{Fore.WHITE}Target: {self.rencana_tahun[tahun]['target']}")
            print(f"{Fore.WHITE}Aktivitas: {self.rencana_tahun[tahun]['aktivitas']}")
            print(f"{Fore.WHITE}Evaluasi: {self.rencana_tahun[tahun]['evaluasi']}")
            print(f"{Fore.WHITE}Milestone: {', '.join(self.milestone_tahunan[tahun])}")

        # Input data baru
        print(f"\n{Fore.CYAN}Masukkan data baru untuk Tahun {tahun}:")
        rencana = input(f"{Fore.WHITE}Masukkan rencana untuk tahun ke-{tahun}: ")
        target = input(f"{Fore.WHITE}Masukkan target yang ingin dicapai: ")
        aktivitas = input(f"{Fore.WHITE}Aktivitas utama yang akan dilakukan: ")
        evaluasi = input(f"{Fore.WHITE}Bagaimana Anda akan mengevaluasi kemajuan: ")
        
        print(f"{Fore.YELLOW}Milestone untuk tahun ke-{tahun} (masukkan 'selesai' jika sudah selesai):")
        milestones = []
        while True:
            milestone = input(f"{Fore.WHITE}Milestone: ")
            if milestone.lower() == 'selesai':
                break
            milestones.append(milestone)

        # Simpan perubahan
        self.rencana_tahun[tahun] = {
            "rencana": rencana,
            "target": target,
            "aktivitas": aktivitas,
            "evaluasi": evaluasi
        }
        self.milestone_tahunan[tahun] = milestones
        
        print(f"\n{Fore.GREEN}Rencana tahun ke-{tahun} berhasil diperbarui!")
        time.sleep(1)

    def edit_profil(self):
        self.display_header("EDIT PROFIL PENGGUNA")
        print(f"{Fore.YELLOW}Profil Saat Ini:")
        print(f"Nama: {self.profil_pengguna['nama']}")
        print(f"Usia: {self.profil_pengguna['usia']}")
        print(f"Pendidikan: {self.profil_pengguna['pendidikan_terakhir']}")
        
        konfirmasi = input(f"\n{Fore.WHITE}Apakah Anda yakin ingin mengubah profil? (y/n): ")
        if konfirmasi.lower() == 'y':
            self.input_profil()


if __name__ == "__main__":
    perencanaan = PerencanaanKarier()
    perencanaan.menu_utama()



