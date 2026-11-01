import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });

export const metadata: Metadata = {
  title: "IFSA's FRTB-SA Auditor — Autonomous Capital & Regulatory Audit Engine",
  description: "IFSA's FRTB-SA Auditor: Drop any Bank Disclosure or Trading Book PDF. We extract the portfolio, audit regulatory compliance, and compute standardised capital charges in real time.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={inter.variable}>
      <body className={`${inter.variable} min-h-screen bg-white text-[#181d26] font-sans antialiased selection:bg-[#e0e2e6] selection:text-[#181d26]`}>
        {children}
      </body>
    </html>
  );
}

