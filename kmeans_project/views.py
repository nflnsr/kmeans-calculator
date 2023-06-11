from django.shortcuts import redirect, render
from django.views import View
from .forms import InputForm
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


# Create your views here.
class Index(View):
    template_name = '../templates/projects/index.html'

    def get(self, request):
        return render(request, '../templates/projects/index.html')

    def post(self, request):
        if request.method == 'POST':
            form = InputForm(request.POST)
            if form.is_valid():
                data1 = form.cleaned_data['data1']
                data2 = form.cleaned_data['data2']
                k = form.cleaned_data['k']

                data1_values = [float(x) for x in data1.split(',')]
                data2_values = [float(x) for x in data2.split(',')]
                k = int(k)

                print(data1_values)
                print(data2_values)
                print(k)

                dataset = np.column_stack((data1_values, data2_values))

                kmeans = KMeans(n_clusters=k, random_state=42)
                kmeans.fit(dataset)


                labels = kmeans.labels_
                centroids = kmeans.cluster_centers_[::-1]

                k = []
                l = []

                for i in range(len(labels)):
                    k.append(f"Data {i+1}: Cluster {labels[i]+1}")
                    
                print(k)

                for i, centroid in enumerate(centroids):
                    l.append(f"Centroid {i+1}: Data1={centroid[0]}, Data2={centroid[1]}")
                
                print(l)


                response = render(request, '../templates/projects/hasil.html', {'k': k, 'l': l})
                response.set_cookie('k', k)
                response.set_cookie('l', l)
                return response

        return render(request, '../templates/projects/index.html')






    # def input_view(self, request):
    #     if request.method == 'POST':
    #         form = InputForm(request.POST)
    #         if form.is_valid():
    #             user_input = form.cleaned_data['user_input']
    #             # lakukan logika Anda berdasarkan user_input
    #             # contoh logika sederhana:
    #             if user_input == 'hello':
    #                 result = 'Halo!'
    #             else:
    #                 result = 'Input tidak valid'
    #             return render(request, 'result.html', {'result': result})
    #     else:
    #         form = InputForm()
    #     return render(request, 'input.html', {'form': form})




# # Fungsi untuk melakukan clustering
# def perform_clustering():
#     # Mendapatkan data1 dan data2 dari entry
#     data1_values = [float(x) for x in entry_data1.get().split(',')]
#     data2_values = [float(x) for x in entry_data2.get().split(',')]

#     # Memasukkan data1 dan data2 ke dalam dataset
#     dataset = np.column_stack((data1_values, data2_values))

#     # Memilih jumlah cluster (k)
#     k = int(entry_clusters.get())

#     # Memuat model K-means dan melakukan clustering
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     kmeans.fit(dataset)

#     # Mendapatkan cluster labels dan centroids
#     labels = kmeans.labels_
#     # Mengganti label 0 dan 1 menjadi 1 dan 2
#     #labels = np.where(labels == 0, 2, 1)  # Menukar label
#     centroids = kmeans.cluster_centers_[::-1]  # Membalik urutan centroids

#     # Menghapus cluster labels dan centroids yang lama
#     for label in frame_cluster_labels.winfo_children():
#         label.destroy()
#     for label in frame_centroids.winfo_children():
#         label.destroy()

#     # Menampilkan cluster labels
#     for i in range(len(labels)):
#         label = tk.Label(frame_cluster_labels, text=f"Data {i+1}: Cluster {labels[i]+1}")
#         label.pack()

#     # Menampilkan centroids
#     for i, centroid in enumerate(centroids):
#         label = tk.Label(frame_centroids, text=f"Centroid {i+1}: Data1={centroid[0]}, Data2={centroid[1]}")
#         label.pack()

# # Fungsi untuk memilih file CSV
# def select_csv_file():
#     file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
#     if file_path:
#         try:
#             dataset = pd.read_csv(file_path)
#             data1_values = dataset.iloc[:, 0].values.tolist()
#             data2_values = dataset.iloc[:, 1].values.tolist()
#             entry_data1.delete(0, tk.END)
#             entry_data1.insert(0, ",".join(str(val) for val in data1_values))
#             entry_data2.delete(0, tk.END)
#             entry_data2.insert(0, ",".join(str(val) for val in data2_values))
#         except Exception as e:
#             print(f"Error: {e}")

# # Fungsi untuk menghapus data
# def clear_data():
#     entry_data1.delete(0, tk.END)
#     entry_data2.delete(0, tk.END)

#     # Menghapus output
#     for label in frame_cluster_labels.winfo_children():
#         label.destroy()
#     for label in frame_centroids.winfo_children():
#         label.destroy()

# # Fungsi untuk menampilkan "About Us"
# def show_about_us():
#     about_us_window = tk.Toplevel(window)
#     about_us_window.title("Our Team")
#     about_us_window.geometry("300x200")
#     label_about_us = tk.Label(about_us_window, text="Data Mining\n\nKelompok 8 K-Means Clustering\n\n- WILDAN ALFARIZI (3337210013)\n- VALDY RAMADHAN (3337210027)\n- NAUFAL NASRULLAH (3337210037)\n- IQBAL MAFTUHA FAUZY(3337210056)\n- FIKRI ASSHIDDIQI(3337210015)\n- MUHAMMAD FADJAR JULIANTO(3337210047)\n- MUHAMMAD CARLO MUZAQI(3337210068)")
#     label_about_us.pack()

# # Fungsi untuk menampilkan "Tech Stack"
# def show_tech():
#     about_us_window = tk.Toplevel(window)
#     about_us_window.title("Tech Stack")
#     about_us_window.geometry("200x190")
#     label_about_us = tk.Label(about_us_window, text="Tech Stack and Library\n\n-Python\n-Tkinter\n-Numpy\n-Pandas\n-Scikit-learn\n-Filedialog")
#     label_about_us.pack()

# # Membuat GUI Window
# window = tk.Tk()
# window.title("K-Means Clustering Kelompok 8")
# window.geometry("500x550")

# # Label Judul
# label_print = tk.Label(window, text="Kelompok 8 K-Means Clustering")
# label_print.pack()

# # Membuat frame untuk data1 input
# frame_data1 = tk.Frame(window)
# frame_data1.pack()

# # Membuat label dan entry untuk data1
# label_data1 = tk.Label(frame_data1, text="Masukan Data1:")
# label_data1.pack(side=tk.LEFT)
# entry_data1 = tk.Entry(frame_data1)
# entry_data1.pack(side=tk.LEFT)

# # Membuat tombol untuk memilih file CSV
# button_csv = tk.Button(frame_data1, text="Select CSV ", command=select_csv_file)
# button_csv.pack(side=tk.LEFT, padx=5)

# # Membuat frame untuk data2 input
# frame_data2 = tk.Frame(window)
# frame_data2.pack()

# # Membuat label dan entry untuk data2
# label_data2 = tk.Label(frame_data2, text="Masukan Data2:")
# label_data2.pack(side=tk.LEFT)
# entry_data2 = tk.Entry(frame_data2)
# entry_data2.pack(side=tk.LEFT)

# # Membuat frame untuk masukan jumlah cluster
# frame_clusters = tk.Frame(window)
# frame_clusters.pack()

# # Membuat label dan entry untuk jumlah cluster
# label_clusters = tk.Label(frame_clusters, text="MasukanCluster:")
# label_clusters.pack(side=tk.LEFT)
# entry_clusters = tk.Entry(frame_clusters)
# entry_clusters.pack(side=tk.LEFT)

# # Membuat tombol tidak berfungsi
# button_temp = tk.Button(frame_clusters, text="Buttonless  ")
# button_temp.pack(side=tk.LEFT, padx=5)

# # Membuat tombol untuk menghapus data
# button_clear = tk.Button(frame_data2, text="Hapus Data", command=clear_data)
# button_clear.pack(side=tk.LEFT, padx=5)

# # Membuat tombol untuk melakukan clustering
# button_cluster = tk.Button(window, text="Perform Clustering", command=perform_clustering)
# button_cluster.pack(pady=10)

# # Membuat tombol untuk menampilkan "About Us"
# button_about_us = tk.Button(window, text="Our Team", command=show_about_us)
# button_about_us.pack(pady=10)

# # Membuat tombol untuk menampilkan "Tech Stack"
# button_tech = tk.Button(window, text="Tech Stack", command=show_tech)
# button_tech.pack()

# # Membuat label untuk instruksi
# label_print = tk.Label(window, text="Note: Masukkan data1 dan data2 dipisahkan dengan koma (,)")
# label_print.pack(pady=10)

# # Membuat frame untuk menampilkan cluster labels dan centroids
# frame_cluster_labels = tk.Frame(window)
# frame_cluster_labels.pack()

# frame_centroids = tk.Frame(window)
# frame_centroids.pack()

# # Run the GUI event loop
# window.mainloop()