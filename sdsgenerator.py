<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chemical Safety Data Sheet (SDS) Generator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .hazard-card {
            transition: all 0.3s ease;
        }
        .hazard-card:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }
        .chemical-image {
            width: 200px;
            height: 200px;
            object-fit: contain;
        }
    </style>
</head>
<body class="bg-gray-50 min-h-screen">
    <div class="container mx-auto px-4 py-8">
        <header class="bg-blue-600 text-white rounded-lg shadow-lg p-6 mb-8">
            <h1 class="text-3xl font-bold">Chemical Safety Data Sheet (SDS) Generator</h1>
            <p class="mt-2">Pengecek Keselamatan Bahan Kimia</p>
        </header>

        <div class="bg-white rounded-lg shadow-md p-6 mb-8">
            <div class="flex flex-col md:flex-row gap-6">
                <div class="flex-1">
                    <h2 class="text-xl font-semibold mb-4">Cari Informasi Bahan Kimia</h2>
                    <div class="flex gap-2">
                        <input 
                            type="text" 
                            id="chemicalName" 
                            placeholder="Masukkan nama bahan kimia" 
                            class="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                        >
                        <button onclick="searchChemical()" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg transition">
                            Cari
                        </button>
                    </div>
                </div>
                
                <div class="flex-shrink-0 flex justify-center items-center">
                    <img 
                        src="https://placehold.co/150" 
                        alt="Chemical compound molecular structure visualization with safety symbols floating around" 
                        class="chemical-image rounded-lg border border-gray-200"
                        id="chemicalImage"
                    >
                </div>
            </div>
        </div>

        <div id="resultContainer" class="hidden">
            <div class="bg-white rounded-lg shadow-md p-6 mb-6">
                <h2 class="text-2xl font-bold mb-4">
                    Hasil Pencarian: 
                    <span id="resultChemicalName" class="text-blue-600"></span>
                </h2>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <h3 class="text-lg font-semibold mb-3">Identifikasi Bahan Kimia</h3>
                        <table class="w-full border-collapse">
                            <tr class="border-b border-gray-200">
                                <td class="py-2 font-medium">Nama Kimia</td>
                                <td id="chemName" class="py-2"></td>
                            </tr>
                            <tr class="border-b border-gray-200">
                                <td class="py-2 font-medium">Rumus Kimia</td>
                                <td id="chemFormula" class="py-2"></td>
                            </tr>
                            <tr class="border-b border-gray-200">
                                <td class="py-2 font-medium">CAS Number</td>
                                <td id="casNumber" class="py-2"></td>
                            </tr>
                            <tr class="border-b border-gray-200">
                                <td class="py-2 font-medium">Klasifikasi Bahaya</td>
                                <td id="hazardClass" class="py-2"></td>
                            </tr>
                        </table>
                    </div>
                    
                    <div>
                        <h3 class="text-lg font-semibold mb-3">Dasar Hukum</h3>
                        <div class="bg-yellow-50 border-l-4 border-yellow-400 p-4">
                            <p class="text-yellow-700">Informasi ini berdasarkan peraturan:</p>
                            <ul class="list-disc pl-5 mt-2 text-yellow-700">
                                <li>Permenaker No. PER.08/MEN/VII/2010</li>
                                <li>Peraturan CLP (Classification, Labelling and Packaging)</li>
                                <li>GHS (Globally Harmonized System)</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-white rounded-lg shadow-md p-6 mb-6">
                <h2 class="text-xl font-semibold mb-4">Simbol Bahaya</h2>
                <div id="hazardSymbols" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 mb-6"></div>
                
                <h3 class="text-lg font-semibold mb-3">Pernyataan Bahaya (H-Phrases)</h3>
                <div id="hPhrases" class="bg-red-50 border-l-4 border-red-500 p-4 mb-6"></div>
                
                <h3 class="text-lg font-semibold mb-3">Pernyataan Peringatan (P-Phrases)</h3>
                <div id="pPhrases" class="bg-blue-50 border-l-4 border-blue-500 p-4 mb-6"></div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div class="bg-white rounded-lg shadow-md p-6">
                    <h2 class="text-xl font-semibold mb-4">Alat Pelindung Diri (APD) yang Diperlukan</h2>
                    <div id="ppeRequired">
                        <div class="flex flex-col gap-4">
                            <div class="flex items-center gap-3 p-3 rounded-lg bg-gray-50 hover:bg-gray-100">
                                <img src="https://placehold.co/60x60" alt="Protective gloves with chemical resistance indicators" class="w-12 h-12">
                                <div>
                                    <h4 class="font-medium">Sarung Tangan Pelindung</h4>
                                    <p class="text-sm text-gray-600">Material yang direkomendasikan akan muncul di sini</p>
                                </div>
                            </div>
                            <!-- More PPE items will be populated by JavaScript -->
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-lg shadow-md p-6">
                    <h2 class="text-xl font-semibold mb-4">Tindakan Pertolongan Pertama</h2>
                    <div id="firstAid" class="space-y-3">
                        <div class="flex gap-3">
                            <div class="flex-shrink-0 w-8 h-8 bg-red-100 text-red-600 rounded-full flex items-center justify-center">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-alert-triangle"><path d="M21.73 18-8-14a2 2 0 0 0-2 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg>
                            </div>
                            <p>Informasi pertolongan pertama akan muncul di sini</p>
                        </div>
                        <!-- More first aid steps will be populated by JavaScript -->
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="bg-white rounded-lg shadow-md p-6">
                    <h2 class="text-xl font-semibold mb-4">Penanganan Tumpahan</h2>
                    <div id="spillHandling" class="space-y-3">
                        <div class="flex gap-3">
                            <div class="flex-shrink-0 w-8 h-8 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-shield-alert"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="M12 8v4"/><path d="M12 16h.01"/></svg>
                            </div>
                            <p>Prosedur penanganan tumpahan akan muncul di sini</p>
                        </div>
                        <!-- More spill handling steps will be populated by JavaScript -->
                    </div>
                </div>
                
                <div class="bg-white rounded-lg shadow-md p-6">
                    <h2 class="text-xl font-semibold mb-4">Tindakan Dalam Keadaan Darurat</h2>
                    <div id="emergencyActions" class="space-y-3">
                        <div class="flex gap-3">
                            <div class="flex-shrink-0 w-8 h-8 bg-red-100 text-red-600 rounded-full flex items-center justify-center">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-siren"><path d="M7 12a5 5 0 0 1 5-5v0a5 5 0 0 1 5 5v6H7v-6Z"/><path d="M5 20a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v2H5v-2Z"/><path d="M21 12h1"/><path d="M18.5 4.5 18 5"/><path d="M2 12h1"/><path d="M12 2v1"/><path d="m4.929 4.929.707.707"/><path d="M12 12v6"/></svg>
                            </div>
                            <p>Prosedur keadaan darurat akan muncul di sini</p>
                        </div>
                        <!-- More emergency actions will be populated by JavaScript -->
                    </div>
                </div>
            </div>
        </div>

        <div id="emptyState" class="text-center py-12">
            <img src="https://placehold.co/300x200" alt="Illustration of a scientist analyzing chemical substances with safety equipment" class="mx-auto mb-6 rounded-lg">
            <h3 class="text-xl font-semibold text-gray-700">Mulai Pencarian Bahan Kimia</h3>
            <p class="text-gray-500 mt-2">Masukkan nama bahan kimia di kolom pencarian untuk melihat informasi keselamatan</p>
        </div>
    </div>

    <script>
        // Chemical database - in a real app this would come from an API
        const chemicalDatabase = {
            "asam sulfat": {
                name: "Asam Sulfat",
                formula: "H₂SO₄",
                cas: "7664-93-9",
                hazardClass: "Korosif, Beracun, Berbahaya bagi Lingkungan",
                hazards: ["flammable", "corrosive", "environment"],
                hPhrases: [
                    "H314: Menyebabkan luka bakar berat pada kulit dan kerusakan mata",
                    "H335: Dapat mengiritasi saluran pernafasan",
                    "H411: Beracun bagi organisme akuatik dengan efek tahan lama"
                ],
                pPhrases: [
                    "P260: Jangan menghirup debu/uap/aerosol",
                    "P280: Gunakan sarung tangan/alat pelindung/pelindung mata/pelindung wajah",
                    "P305 + P351 + P338: JIKA TERKENA MATA: Bilas dengan hati-hati dengan air selama beberapa menit. Lepaskan lensa kontak jika ada dan bisa dilakukan dengan mudah. Lanjutkan membilas"
                ],
                ppe: [
                    {
                        name: "Sarung Tangan Tahan Kimia",
                        desc: "Sarung tangan nitril atau neoprene",
                        image: "https://placehold.co/60x60?text=Gloves"
                    },
                    {
                        name: "Pelindung Wajah",
                        desc: "Pelindung wajah tahan percikan",
                        image: "https://placehold.co/60x60?text=Face+Shield"
                    },
                    {
                        name: "Apron Tahan Asam",
                        desc: "Apron PVC atau karet",
                        image: "https://placehold.co/60x60?text=Apron"
                    }
                ],
                firstAid: [
                    "Hirup udara segar dan istirahat dalam posisi yang nyaman",
                    "Jika terjadi kontak kulit: Lepaskan pakaian yang terkontaminasi. Bilas kulit dengan air selama minimal 15 menit",
                    "Jika terkena mata: Bilas dengan hati-hati dengan air selama beberapa menit",
                    "Jika tertelan: Berkumur. Jangan induksi muntah"
                ],
                spillHandling: [
                    "Evakuasi area, hindari menghirup uap",
                    "Pakai APD yang memadai (lihat bagian APD)",
                    "Netralkan dengan natrium bikarbonat atau zat penetral asam lainnya",
                    "Tampung limbah dalam wadah tahan korosi untuk dibuang sesuai peraturan"
                ],
                emergencyActions: [
                    "Dalam kasus kebakaran: Gunakan alat pemadam yang cocok (karbon dioksida, bubuk kering)",
                    "Jika terjadi tumpahan besar atau kebakaran: Hubungi pemadam kebakaran",
                    "Berikan pertolongan pertama sesuai petunjuk",
                    "Jika diperlukan, bawa ke fasilitas medis dengan SDS"
                ],
                image: "https://placehold.co/300x200?text=Asam+Sulfat"
            },
            "metanol": {
                name: "Metanol",
                formula: "CH₃OH",
                cas: "67-56-1",
                hazardClass: "Mudah Terbakar, Beracun",
                hazards: ["flammable", "toxic"],
                hPhrases: [
                    "H225: Sangat mudah terbakar dan mudah menguap",
                    "H301 + H311 + H331: Beracun jika tertelan, kontak dengan kulit atau terhirup",
                    "H370: Menyebabkan kerusakan organ"
                ],
                pPhrases: [
                    "P210: Jauhkan dari panas/percikan/api/nyala",
                    "P280: Gunakan sarung tangan/alat pelindung/pelindung mata/pelindung wajah",
                    "P310: Segera hubungi PUSAT PENGENDALIAN RACUN atau dokter"
                ],
                ppe: [
                    {
                        name: "Sarung Tahan Pelarut",
                        desc: "Sarung tangan butil",
                        image: "https://placehold.co/60x60?text=Gloves"
                    },
                    {
                        name: "Respirator",
                        desc: "Respirator dengan filter uap organik",
                        image: "https://placehold.co/60x60?text=Respirator"
                    },
                    {
                        name: "Kacamata Pelindung",
                        desc: "Kacamata pengaman tahan percikan",
                        image: "https://placehold.co/60x60?text=Goggles"
                    }
                ],
                firstAid: [
                    "Jika tertelan: Jangan menginduksi muntah. Segera cari pertolongan medis",
                    "Jika terkena kulit: Cuci dengan sabun dan air mengalir",
                    "Jika terhirup: Pindahkan ke udara segar, pertahankan agar tetap hangat dan istirahat",
                    "Jika terkena mata: Bilas dengan air mengalir selama 15 menit"
                ],
                spillHandling: [
                    "Hilangkan semua sumber penyalaan",
                    "Pakai APD lengkap termasuk respirator",
                    "Trik dengan bahan penyerap yang tidak mudah terbakar (pasir, vermikulit)",
                    "Tempatkan dalam wadah tertutup dan berlabel"
                ],
                emergencyActions: [
                    "Kebakaran kecil: Gunakan CO₂, busa, atau bubuk kering",
                    "Kebakaran besar: Gunakan penyemprot air atau busa tahan alkohol",
                    "Jangan menggunakan jet air langsung",
                    "Dalam kasus kebocoran besar: Evakuasi area"
                ],
                image: "https://placehold.co/300x200?text=Metanol"
            },
            "natrium hidroksida": {
                name: "Natrium Hidroksida",
                formula: "NaOH",
                cas: "1310-73-2",
                hazardClass: "Korosif",
                hazards: ["corrosive"],
                hPhrases: [
                    "H290: Dapat bersifat korosif terhadap logam",
                    "H314: Menyebabkan luka bakar berat pada kulit dan kerusakan mata"
                ],
                pPhrases: [
                    "P280: Gunakan sarung tangan/alat pelindung/pelindung mata/pelindung wajah",
                    "P301 + P330 + P331: JIKA TERTELAN: Berkumur-kumur. JANGAN MEMBUAT MUNTAH",
                    "P305 + P351 + P338: JIKA TERKENA MATA: Bilas dengan hati-hati dengan air selama beberapa menit"
                ],
                ppe: [
                    {
                        name: "Sarung Tahan Alkali",
                        desc: "Sarung tangan karet atau neoprene",
                        image: "https://placehold.co/60x60?text=Gloves"
                    },
                    {
                        name: "Apron Plastik",
                        desc: "Apron PVC tahan bahan kimia",
                        image: "https://placehold.co/60x60?text=Apron"
                    },
                    {
                        name: "Pelindung Muka",
                        desc: "Pelindung wajah tahan percikan",
                        image: "https://placehold.co/60x60?text=Face+Shield"
                    }
                ],
                firstAid: [
                    "Jika tertelan: Berkumur dengan air, jangan menginduksi muntah",
                    "Jika terkena kulit: Bilas dengan air mengalir selama 15 menit",
                    "Jika terkena mata: Bilas dengan air mengalir selama minimal 15 menit",
                    "Jika terhirup: Pindahkan ke udara segar"
                ],
                spillHandling: [
                    "Pakai APD lengkap termasuk pelindung pernafasan jika debu",
                    "Netralkan dengan asam encer (contoh: cuka)",
                    "Bersihkan dengan air dalam jumlah besar",
                    "Kumpulkan cairan untuk dibuang"
                ],
                emergencyActions: [
                    "Dalam kasus kebakaran: Gunakan air dalam jumlah banyak",
                    "Hindari kontak dengan logam aluminium (menghasilkan gas hidrogen mudah terbakar)",
                    "Jika tertelan dalam jumlah besar: Bawa ke rumah sakit dengan SDS"
                ],
                image: "https://placehold.co/300x200?text=Natrium+Hidroksida"
            }
        };

        const hazardSymbols = {
            "flammable": {
                name: "Mudah Terbakar",
                image: "https://placehold.co/100x100/FF5733/FFFFFF?text=🔥",
                description: "Zat dan campuran yang mudah terbakar"
            },
            "corrosive": {
                name: "Korosif",
                image: "https://placehold.co/100x100/FFC300/FFFFFF?text=⚠️",
                description: "Dapat menyebabkan luka bakar pada kulit dan korosi pada logam"
            },
            "toxic": {
                name: "Beracun",
                image: "https://placehold.co/100x100/900C3F/FFFFFF?text=☠️",
                description: "Beracun jika tertelan, terhirup, atau kontak dengan kulit"
            },
            "environment": {
                name: "Berbahaya Lingkungan",
                image: "https://placehold.co/100x100/1E8449/FFFFFF?text=🌍",
                description: "Berbahaya bagi organisme akuatik atau lingkungan"
            },
            "health-hazard": {
                name: "Bahaya Kesehatan",
                image: "https://placehold.co/100x100/8E44AD/FFFFFF?text=⚠️",
                description: "Dapat menyebabkan efek kesehatan jangka panjang"
            }
        };

        function searchChemical() {
            const input = document.getElementById('chemicalName');
            const chemicalName = input.value.trim().toLowerCase();
            
            if (!chemicalName) {
                alert('Silahkan masukkan nama bahan kimia');
                return;
            }
            
            const chemical = chemicalDatabase[chemicalName];
            
            if (chemical) {
                document.getElementById('resultContainer').classList.remove('hidden');
                document.getElementById('emptyState').classList.add('hidden');
                
                // Set basic info
                document.getElementById('resultChemicalName').textContent = chemical.name;
                document.getElementById('chemName').textContent = chemical.name;
                document.getElementById('chemFormula').textContent = chemical.formula;
                document.getElementById('casNumber').textContent = chemical.cas;
                document.getElementById('hazardClass').textContent = chemical.hazardClass;
                document.getElementById('chemicalImage').src = chemical.image;
                
                // Set hazard symbols
                const hazardSymbolsContainer = document.getElementById('hazardSymbols');
                hazardSymbolsContainer.innerHTML = '';
                
                chemical.hazards.forEach(hazard => {
                    const symbol = hazardSymbols[hazard];
                    if (symbol) {
                        const card = document.createElement('div');
                        card.className = 'hazard-card bg-white p-4 rounded-lg border border-gray-200 flex flex-col items-center text-center';
                        card.innerHTML = `
                            <img src="${symbol.image}" alt="${symbol.name} - ${symbol.description}" class="w-16 h-16 mb-2">
                            <h4 class="font-semibold">${symbol.name}</h4>
                            <p class="text-sm text-gray-600">${symbol.description}</p>
                        `;
                        hazardSymbolsContainer.appendChild(card);
                    }
                });
                
                // Set H and P phrases
                const hPhrasesContainer = document.getElementById('hPhrases');
                hPhrasesContainer.innerHTML = '<ul class="list-disc space-y-1">' + 
                    chemical.hPhrases.map(phrase => `<li>${phrase}</li>`).join('') + '</ul>';
                
                const pPhrasesContainer = document.getElementById('pPhrases');
                pPhrasesContainer.innerHTML = '<ul class="list-disc space-y-1">' + 
                    chemical.pPhrases.map(phrase => `<li>${phrase}</li>`).join('') + '</ul>';
                
                // Set PPE
                const ppeContainer = document.getElementById('ppeRequired');
                ppeContainer.innerHTML = '<div class="flex flex-col gap-4">' + 
                    chemical.ppe.map(item => `
                        <div class="flex items-center gap-3 p-3 rounded-lg bg-gray-50 hover:bg-gray-100">
                            <img src="${item.image}" alt="${item.name + ' - ' + item.desc}" class="w-12 h-12">
                            <div>
                                <h4 class="font-medium">${item.name}</h4>
                                <p class="text-sm text-gray-600">${item.desc}</p>
                            </div>
                        </div>
                    `).join('') + '</div>';
                
                // Set first aid
                const firstAidContainer = document.getElementById('firstAid');
                firstAidContainer.innerHTML = chemical.firstAid.map((step, index) => `
                    <div class="flex gap-3">
                        <div class="flex-shrink-0 w-8 h-8 bg-red-100 text-red-600 rounded-full flex items-center justify-center">
                            ${index + 1}
                        </div>
                        <p>${step}</p>
                    </div>
                `).join('');
                
                // Set spill handling
                const spillHandlingContainer = document.getElementById('spillHandling');
                spillHandlingContainer.innerHTML = chemical.spillHandling.map((step, index) => `
                    <div class="flex gap-3">
                        <div class="flex-shrink-0 w-8 h-8 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center">
                            ${index + 1}
                        </div>
                        <p>${step}</p>
                    </div>
                `).join('');
                
                // Set emergency actions
                const emergencyActionsContainer = document.getElementById('emergencyActions');
                emergencyActionsContainer.innerHTML = chemical.emergencyActions.map((step, index) => `
                    <div class="flex gap-3">
                        <div class="flex-shrink-0 w-8 h-8 bg-red-100 text-red-600 rounded-full flex items-center justify-center">
                            ${index + 1}
                        </div>
                        <p>${step}</p>
                    </div>
                `).join('');
                
            } else {
                alert('Bahan kimia tidak ditemukan dalam database. Coba bahan kimia lain seperti "asam sulfat", "metanol", atau "natrium hidroksida"');
            }
        }
    </script>
</body>
</html>
