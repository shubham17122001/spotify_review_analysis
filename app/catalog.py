# Spotify Mock Track Catalog for AI Discovery Engine

TRACKS = [
    # --- MAINSTREAM / MAJOR LABEL ---
    {
        "id": 1,
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "genre": "Synth-pop / Dance-pop",
        "popularity": 98,
        "label_type": "Major",
        "sonic_description": "High-tempo 1980s-retro synth-pop with driving basslines, dramatic vocals, and bright, shimmering synthesizers. High energy, dark city lights, nocturnal vibe.",
        "vibes": ["energetic", "nocturnal", "retro", "synth-heavy", "driving"]
    },
    {
        "id": 2,
        "title": "Bad Guy",
        "artist": "Billie Eilish",
        "genre": "Alt-pop / Dark pop",
        "popularity": 92,
        "label_type": "Major",
        "sonic_description": "Minimalist pop with heavy, thumping electronic sub-bass, whispered vocals, and quirky, playful synthesizer hooks. Dark, tongue-in-cheek, quiet intensity.",
        "vibes": ["minimalist", "dark", "sub-bass", "whispery", "quirky"]
    },
    {
        "id": 3,
        "title": "Anti-Hero",
        "artist": "Taylor Swift",
        "genre": "Synth-pop / Pop",
        "popularity": 95,
        "label_type": "Major",
        "sonic_description": "Mid-tempo self-reflective pop with clean, drum-machine beats, warm synth pads, and highly melodic vocal lines. Melancholic yet catchy, introspective.",
        "vibes": ["melancholic", "introspective", "catchy", "warm", "clean"]
    },
    {
        "id": 4,
        "title": "As It Was",
        "artist": "Harry Styles",
        "genre": "Indie pop / New wave",
        "popularity": 94,
        "label_type": "Major",
        "sonic_description": "Upbeat, breezy new wave track with upbeat bells, ringing electric guitars, and a rapid, pulsing drum groove. Lighthearted melody concealing melancholic lyrics.",
        "vibes": ["breezy", "upbeat", "nostalgic", "guitar-driven", "melancholic"]
    },
    {
        "id": 5,
        "title": "Starboy",
        "artist": "The Weeknd ft. Daft Punk",
        "genre": "R&B / Synth-pop",
        "popularity": 93,
        "label_type": "Major",
        "sonic_description": "Moody, dark R&B with a crisp electronic drum groove, gritty synthesized basslines, and Daft Punk's robotic backing vocals. Confident, urban, late-night driving vibe.",
        "vibes": ["moody", "late-night", "robotic", "gritty", "urban"]
    },
    {
        "id": 6,
        "title": "Cruel Summer",
        "artist": "Taylor Swift",
        "genre": "Pop / Synth-pop",
        "popularity": 96,
        "label_type": "Major",
        "sonic_description": "Explosive, dramatic pop with soaring vocals, distorted vocal synths in the background, and a pounding, emotional beat. Euphoric, summer heat, high-energy vocals.",
        "vibes": ["euphoric", "dramatic", "emotional", "explosive", "vocals"]
    },
    {
        "id": 7,
        "title": "Flowers",
        "artist": "Miley Cyrus",
        "genre": "Pop / Disco",
        "popularity": 90,
        "label_type": "Major",
        "sonic_description": "Mid-tempo retro disco-pop with a warm bassline, strutting groove, clean electric guitar chords, and confident, raspy vocals. Empowering, summery, self-love vibe.",
        "vibes": ["empowering", "disco", "warm", "summery", "raspy-vocals"]
    },
    {
        "id": 8,
        "title": "Levitating",
        "artist": "Dua Lipa",
        "genre": "Dance-pop / Nu-disco",
        "popularity": 91,
        "label_type": "Major",
        "sonic_description": "High-energy nu-disco track with a bouncy slap-bass line, handclaps, funk-style guitar scratches, and spacey, upbeat vocals. Fun, spacey, highly danceable.",
        "vibes": ["danceable", "bouncy", "funk-guitar", "spacey", "upbeat"]
    },

    # --- MID-TIER / CROSSOVER INDEPENDENT ---
    {
        "id": 10,
        "title": "Texas Sun",
        "artist": "Leon Bridges & Khruangbin",
        "genre": "Soul / Psychedelic Rock",
        "popularity": 78,
        "label_type": "Independent",
        "sonic_description": "Slow, breezy soul-rock with warm, delay-soaked psychedelic electric guitars, smooth R&B vocals, and a gentle, rolling drum groove. Sun-drenched, road trip, relaxing vibe.",
        "vibes": ["breezy", "psychedelic", "soulful", "relaxing", "sun-drenched"]
    },
    {
        "id": 11,
        "title": "10%",
        "artist": "Kaytranada ft. Kali Uchis",
        "genre": "Electronic / Neo-Soul",
        "popularity": 74,
        "label_type": "Independent",
        "sonic_description": "Funky house groove with syncopated electronic beats, a deep rubbery bassline, and Kali Uchis's sultry, smooth vocals. Club vibe, swagger, groovy dance-pop.",
        "vibes": ["funky", "groovy", "sultry", "electronic-beats", "smooth"]
    },
    {
        "id": 12,
        "title": "Holocene",
        "artist": "Bon Iver",
        "genre": "Indie folk / Ambient",
        "popularity": 75,
        "label_type": "Independent",
        "sonic_description": "Intricate, soft acoustic guitar picking patterns, swell-like ambient brass, and Justin Vernon's delicate, fragile falsetto vocals. Majestic, icy, deeply emotional, quiet.",
        "vibes": ["acoustic", "ambient", "falsetto", "majestic", "emotional"]
    },
    {
        "id": 13,
        "title": "Redbone",
        "artist": "Childish Gambino",
        "genre": "Funk / R&B",
        "popularity": 85,
        "label_type": "Major",
        "sonic_description": "Slow-tempo psychedelic funk with a massive, fuzzy bassline, ringing glockenspiel chords, and pitch-shifted, soulful falsetto. Nocturnal, high-drama, smooth funk.",
        "vibes": ["psychedelic", "funk", "fuzzy-bass", "falsetto", "nocturnal"]
    },
    {
        "id": 14,
        "title": "Motion Sickness",
        "artist": "Phoebe Bridgers",
        "genre": "Indie Rock / Alt-pop",
        "popularity": 77,
        "label_type": "Independent",
        "sonic_description": "Mid-tempo indie rock with driving, fuzzy electric guitars, melancholic singer-songwriter vocals, and a steady drumbeat. Nostalgic, bitter-sweet, emotional storytelling.",
        "vibes": ["indie-rock", "guitar-driven", "melancholic", "storytelling", "bitter-sweet"]
    },
    {
        "id": 15,
        "title": "So Good at Being in Trouble",
        "artist": "Unknown Mortal Orchestra",
        "genre": "Psychedelic Pop / Indie R&B",
        "popularity": 72,
        "label_type": "Independent",
        "sonic_description": "Warm, tape-saturated lo-fi indie R&B with lazy, soul-style drums, phasing electric guitars, and gentle, laid-back vocals. Hazy, nostalgic, slow-dance vibe.",
        "vibes": ["lo-fi", "laid-back", "hazy", "nostalgic", "tape-saturated"]
    },

    # --- OBSCURE / NICHE / TRUE INDEPENDENT (Niche Boost targets) ---
    {
        "id": 20,
        "title": "Automatic",
        "artist": "Mildlife",
        "genre": "Psychedelic Jazz / Space Disco",
        "popularity": 45,
        "label_type": "Independent",
        "sonic_description": "Hypnotic, long-form jazz-fusion with a steady, motorik krautrock beat, analog synthesizer sweeps, and intricate, jazz-tinged flute solos. Spacey, immersive, groove-focused.",
        "vibes": ["hypnotic", "spacey", "jazz-fusion", "flute-solo", "analog-synth"]
    },
    {
        "id": 21,
        "title": "Wildfires",
        "artist": "SAULT",
        "genre": "Neo-Soul / Post-Punk",
        "popularity": 55,
        "label_type": "Independent",
        "sonic_description": "Deeply emotional soul track with a heavy, raw bass guitar line, sparse drums, and hauntingly beautiful, whispery female vocals. Melancholic yet defiant, minimal instrumentation.",
        "vibes": ["soulful", "heavy-bass", "haunting", "minimalist", "female-vocals"]
    },
    {
        "id": 22,
        "title": "Dawn Chorus",
        "artist": "Thom Yorke",
        "genre": "Ambient / IDM",
        "popularity": 52,
        "label_type": "Independent",
        "sonic_description": "Minimalist ambient electronica built around a warm, pulsing, detuned synthesizer chord progression. Thom Yorke's low, spoken-word style vocals. Introspective, cold, beautiful, glitchy.",
        "vibes": ["ambient", "pulse", "synthesizer", "spoken-word", "introspective"]
    },
    {
        "id": 23,
        "title": "Keep Moving",
        "artist": "Jungle",
        "genre": "Nu-disco / Neo-soul",
        "popularity": 68,
        "label_type": "Independent",
        "sonic_description": "Uplifting, high-tempo disco-soul with swelling orchestral strings, falsetto choir vocals, and a pounding four-on-the-floor beat. Highly energetic, sunny, celebratory.",
        "vibes": ["uplifting", "disco", "strings", "choir", "celebratory"]
    },
    {
        "id": 24,
        "title": "Dawn In The Adityas",
        "artist": "Ichiko Aoba",
        "genre": "Chamber Folk / Ambient",
        "popularity": 40,
        "label_type": "Independent",
        "sonic_description": "Extremely quiet, delicate Japanese chamber folk. Features sparse, echoing classical acoustic guitar chords and ethereal, crystal-clear vocals. Like a forest clearing in the morning mist.",
        "vibes": ["ethereal", "acoustic", "delicate", "quiet", "forest-mist"]
    },
    {
        "id": 25,
        "title": "Organic Mind",
        "artist": "Alfa Mist",
        "genre": "Jazz / Neo-Soul",
        "popularity": 48,
        "label_type": "Independent",
        "sonic_description": "Intricate contemporary UK jazz featuring a warm electric piano (Fender Rhodes), dynamic jazz drumming, and a smooth trumpet solo. Late-night urban cafe atmosphere, mellow, complex.",
        "vibes": ["jazz", "electric-piano", "mellow", "trumpet-solo", "urban-cafe"]
    },
    {
        "id": 26,
        "title": "Astral Travelling",
        "artist": "Pharoah Sanders",
        "genre": "Spiritual Jazz / Avant-Garde",
        "popularity": 42,
        "label_type": "Independent",
        "sonic_description": "Slow, meditative spiritual jazz with gentle piano ripples, soft shaking percussion, and a floating, celestial saxophone line. Transcendent, cosmic, peaceful, slow-tempo.",
        "vibes": ["spiritual-jazz", "meditative", "cosmic", "celestial", "transcendent"]
    },
    {
        "id": 27,
        "title": "Runnas",
        "artist": "Yussef Dayes ft. Chronixx",
        "genre": "Afro-Jazz / Reggae",
        "popularity": 51,
        "label_type": "Independent",
        "sonic_description": "High-skill jazz drumming with afrobeat syncopations, warm dub basslines, and soulful reggae vocal hooks. Rhythmic, warm, street vibe, active drums.",
        "vibes": ["rhythmic", "jazz-drumming", "afrobeat", "dub-bass", "soulful"]
    },
    {
        "id": 28,
        "title": "Silver Into Gold",
        "artist": "Say She She",
        "genre": "Discodelic / Soul",
        "popularity": 44,
        "label_type": "Independent",
        "sonic_description": "Harmonized, retro-chic female vocals over a funky, psychedelic disco backing track. Think 1970s Chic mixed with dreamy indie-pop. Groovy, vocal harmonies, warm analog instrumentation.",
        "vibes": ["retro", "disco-funk", "dreamy", "harmonies", "analog"]
    },
    {
        "id": 29,
        "title": "Kiasmos",
        "artist": "Looped",
        "genre": "Minimal Techno / Neoclassical",
        "popularity": 50,
        "label_type": "Independent",
        "sonic_description": "Hypnotic blend of a soft, acoustic upright piano loop and sharp, ticking minimal techno glitch beats. Slowly builds up with melancholic strings. Cold, rhythmic, cinematic.",
        "vibes": ["cinematic", "piano-loop", "minimal-techno", "glitchy", "melancholic"]
    },
    {
        "id": 30,
        "title": "Pink Moon",
        "artist": "Nick Drake",
        "genre": "Folk / Singer-songwriter",
        "popularity": 64,
        "label_type": "Independent",
        "sonic_description": "Fragile, beautiful acoustic guitar picking with a low, intimate vocal style and a simple, brief piano chord overlay. Sparse, raw, lonely, autumnal.",
        "vibes": ["acoustic", "intimate", "autumnal", "lonely", "raw"]
    },
    {
        "id": 31,
        "title": "Glowed Up",
        "artist": "Kaytranada ft. Anderson .Paak",
        "genre": "Electronic / Hip-Hop",
        "popularity": 70,
        "label_type": "Independent",
        "sonic_description": "Off-beat, squelchy electronic synth-funk beat with Anderson .Paak's hyperactive, raspy rap and R&B vocals. Bouncy, glitchy, high-swagger, late-night driving.",
        "vibes": ["synths", "funky", "off-beat", "swagger", "rhythmic"]
    },
    {
        "id": 32,
        "title": "So We Won't Forget",
        "artist": "Khruangbin",
        "genre": "Psychedelic Soul / Chill",
        "popularity": 73,
        "label_type": "Independent",
        "sonic_description": "Bubbly, delay-drenched guitar melody, warm rolling bass, and soft, sweet whispers of female backing vocals. Laid-back, nostalgic, comforting, summery.",
        "vibes": ["chill", "bubbly-guitar", "nostalgic", "summery", "relaxing"]
    },
    {
        "id": 33,
        "title": "Roygbiv",
        "artist": "Boards of Canada",
        "genre": "IDM / Downtempo",
        "popularity": 60,
        "label_type": "Independent",
        "sonic_description": "Nostalgic, warm, analog synthesizer melody with a chunky, slow hip-hop style drumbeat. Sounds like a dusty VHS tape from a childhood science show. Cozy, psychedelic, retro-electronic.",
        "vibes": ["analog-synths", "cozy", "dusty-vhs", "psychedelic", "slow-groove"]
    },
    {
        "id": 34,
        "title": "Mary",
        "artist": "Big Thief",
        "genre": "Indie Folk / Chamber Pop",
        "popularity": 66,
        "label_type": "Independent",
        "sonic_description": "Richly textured indie folk with a warm, pipe-organ-like synth backing and intimate acoustic piano. Adrianne Lenker's raw, cracking, highly emotional vocals. Devastatingly beautiful, poetic.",
        "vibes": ["pipe-organ", "piano", "emotional-vocals", "raw", "poetic"]
    },
    {
        "id": 35,
        "title": "A Walk",
        "artist": "Tycho",
        "genre": "Ambient / Chillwave",
        "popularity": 65,
        "label_type": "Independent",
        "sonic_description": "Warm, sunny ambient synth-pop. A rhythmic electronic beat overlays clean, retro synthesizer leads and soft guitar picks. Uplifting, nostalgic, sunrise vibe, driving down a coast.",
        "vibes": ["warm-synths", "sunrise", "uplifting", "nostalgic", "coastal"]
    }
]
