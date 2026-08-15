import type { Metadata } from "next";
import { Inter, JetBrains_Mono, Newsreader } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });
const jetbrains = JetBrains_Mono({ subsets: ["latin"], variable: "--font-mono", weight: ["400","500","600","700"] });
const newsreader = Newsreader({ subsets: ["latin"], variable: "--font-serif", style: ["normal", "italic"] });

export const metadata: Metadata = {
  title: "IFSA's FRTB-SA Auditor — Autonomous Capital & Regulatory Audit Engine",
  description: "IFSA's FRTB-SA Auditor: Drop any Bank Disclosure or Trading Book PDF. We extract the portfolio, audit regulatory compliance, and compute standardised capital charges in real time.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${inter.variable} ${jetbrains.variable} ${newsreader.variable}`}>
      <body className="min-h-screen bg-[#FAF9F6] text-[#0F172A] font-sans antialiased selection:bg-[#FDE68A] selection:text-[#0F172A]">
        {children}
      </body>
    </html>
  );
}

