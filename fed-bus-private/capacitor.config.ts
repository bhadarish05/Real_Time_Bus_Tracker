import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'app.lovable.c2cfbc467a44431e8b2d20d873d7d5f1',
  appName: 'fed-bus-private',
  webDir: 'dist',
  server: {
    url: 'https://c2cfbc46-7a44-431e-8b2d-20d873d7d5f1.lovableproject.com?forceHideBadge=true',
    cleartext: true
  },
  plugins: {
    CapacitorGoogleMaps: {
      iosApiKey: 'YOUR_IOS_API_KEY_HERE',
      androidApiKey: 'YOUR_ANDROID_API_KEY_HERE'
    }
  }
};

export default config;