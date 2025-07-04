import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
});

export const metadata: Metadata = {
  title: "BPM Analyzer - Audio Beat Detection",
  description: "Advanced client-side BPM analysis from audio recordings. Analyze beats per minute, tempo, and rhythm entirely in your browser.",
  keywords: ["BPM", "beat detection", "tempo", "audio analysis", "music", "client-side"],
  authors: [{ name: "BPM Analyzer" }],
  viewport: "width=device-width, initial-scale=1",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${inter.variable} font-sans antialiased`}>
        {children}
      </body>
    </html>
  );
}
