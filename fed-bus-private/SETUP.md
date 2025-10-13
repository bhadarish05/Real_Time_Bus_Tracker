# Privacy-First Bus Tracker Setup Guide

## 🗝️ Google Maps API Setup

### 1. Get API Key
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable these APIs:
   - Maps JavaScript API
   - Directions API  
   - Places API
4. Create credentials → API Key
5. Restrict the key to your domains for security

### 2. Add to Supabase (Recommended)
Since your project has Supabase enabled:
1. Go to Supabase Dashboard → Project Settings → API
2. Add your Google Maps API key as a secret named `GOOGLE_MAPS_API_KEY`

### 3. Temporary Setup (Testing)
For quick testing, the app will prompt you to enter the API key directly.

## 📱 Android Deployment

### Prerequisites
- Node.js installed
- Android Studio installed
- Java JDK 11 or higher

### Steps to Deploy to Android

1. **Export to GitHub**
   ```bash
   # Click "Export to GitHub" button in Lovable
   git clone <your-github-repo-url>
   cd <your-project-name>
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Initialize Capacitor** (already done)
   ```bash
   npx cap init
   ```

4. **Add Android Platform**
   ```bash
   npx cap add android
   ```

5. **Build the Web App**
   ```bash
   npm run build
   ```

6. **Sync with Android**
   ```bash
   npx cap sync android
   ```

7. **Run on Android**
   ```bash
   npx cap run android
   ```

### For Physical Device
1. Enable Developer Options on your Android device
2. Enable USB Debugging
3. Connect via USB
4. Run `npx cap run android` and select your device

## 💻 Local Development

### 1. Export and Clone
```bash
# Click "Export to GitHub" in Lovable
git clone <your-github-repo-url>
cd <your-project-name>
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Run Development Server
```bash
npm run dev
```

### 4. Access Locally
Open `http://localhost:5173` in your browser

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:
```
VITE_GOOGLE_MAPS_API_KEY=your_api_key_here
```

### Mobile Configuration
Edit `capacitor.config.ts` to update:
- Google Maps API keys for iOS/Android
- App name and ID
- Server URL (for development)

## 🛠️ Development Workflow

1. **Web Development**: Use Lovable or local development
2. **Mobile Testing**: 
   ```bash
   npm run build
   npx cap sync
   npx cap run android # or ios
   ```
3. **Production**: Deploy web version, build mobile apps for app stores

## 📚 Next Steps

1. Set up Google Maps API key
2. Test the web version locally
3. Deploy to Android device
4. Integrate with your Python FastAPI backend
5. Add real federated learning models

## 🆘 Troubleshooting

- **Maps not loading**: Check API key and enabled APIs
- **Android build fails**: Ensure Android Studio and JDK are properly installed
- **Capacitor sync issues**: Run `npx cap clean` then `npx cap sync`

## 📖 Documentation
- [Capacitor Documentation](https://capacitorjs.com/docs)
- [Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript)
- [Lovable Mobile Development](https://lovable.dev/blogs/TODO)