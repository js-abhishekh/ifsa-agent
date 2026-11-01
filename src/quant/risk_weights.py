"""
src/quant/risk_weights.py

Static Basel Annex risk weight and correlation tables for FRTB-SA.

These tables are sourced directly from the BCBS MAR document (MAR21 for SBM,
MAR22 for DRC, MAR23 for RRAO). They serve two purposes:

  1. Ground-truth fallback when the LLM extraction fails or returns incomplete data.
  2. Hallucination-check reference: LLM-extracted values are validated against
     these tables within RISK_WEIGHT_TOLERANCE; divergence raises a ValidationError.

All rates are expressed as decimals (e.g. 0.015 = 1.5%).
Correlation matrices: keys are "bucket_i_bucket_j" (i < j) or "default".

Reference: BCBS Basel III finalisation (Dec 2017, rev. Jul 2019, Jan 2023).
"""

from typing import Dict

# ── GIRR (MAR21.44–21.53) ─────────────────────────────────────────────────────
# Risk weights by tenor (both yield curve and inflation buckets)
GIRR_RISK_WEIGHTS: Dict[str, float] = {
    "0.25Y": 0.017,
    "0.5Y":  0.017,
    "1Y":    0.016,
    "2Y":    0.013,
    "3Y":    0.012,
    "5Y":    0.011,
    "10Y":   0.011,
    "15Y":   0.011,
    "20Y":   0.011,
    "30Y":   0.011,
    "inflation": 0.016,
    "cross_currency_basis": 0.016,
    # Currency bucket and baseline defaults (standard BCBS 1Y/5Y intermediate rate)
    "default": 0.016,
    "INR":     0.016,
    "USD":     0.016,
    "EUR":     0.016,
    "GBP":     0.016,
    "JPY":     0.016,
}

# Within-bucket (same currency) tenor correlations (ρ_kl = exp(-α|T_k - T_l|))
# α = 0.03 per MAR21.47; pre-computed for common pairs
GIRR_CORRELATIONS: Dict[str, float] = {
    # same-bucket, cross-tenor correlations
    "rho_default": 0.999,   # approximate for same-tenor, different curves
    "1Y_5Y":   0.905,
    "1Y_10Y":  0.819,
    "5Y_10Y":  0.905,
    "5Y_30Y":  0.741,
    "10Y_30Y": 0.819,
    # cross-bucket (different currency) gamma
    "gamma_bc": 0.42,
}

# ── Equity (MAR21.71–21.80) ────────────────────────────────────────────────────
# Buckets 1–11; weights are percentage risk weights (as decimals)
EQUITY_RISK_WEIGHTS: Dict[str, float] = {
    # Large-cap EM
    "1":  0.55,   # EM large-cap consumer goods/services
    "2":  0.60,   # EM large-cap telecoms / industrials
    "3":  0.45,   # EM large-cap basic materials / energy / agriculture
    "4":  0.55,   # EM large-cap financials / real estate
    # Large-cap DM
    "5":  0.30,   # DM large-cap consumer goods/services
    "6":  0.35,   # DM large-cap telecoms / industrials
    "7":  0.40,   # DM large-cap basic materials / energy / agriculture
    "8":  0.50,   # DM large-cap financials / real estate
    # Small-cap
    "9":  0.70,   # EM small-cap (all sectors)
    "10": 0.50,   # DM small-cap (all sectors)
    "11": 0.70,   # Indices / ETFs / other (residual)
    # Convenience aliases
    "EM_LargeCap": 0.55,
    "DM_LargeCap": 0.35,
    "EM_SmallCap": 0.70,
    "DM_SmallCap": 0.50,
    "default":     0.55,
}

EQUITY_CORRELATIONS: Dict[str, float] = {
    # Within-bucket same-name (intra)
    "rho_intra_same_issuer": 0.999,
    # Within-bucket different names — varies by bucket; use conservative default
    "rho_intra_default": 0.25,
    # Cross-bucket gamma
    "gamma_bc_same_em":  0.15,
    "gamma_bc_same_dm":  0.15,
    "gamma_bc_em_dm":    0.075,
    "gamma_bc_index":    0.075,
    "gamma_bc_default":  0.15,
}

# ── CSR Non-Securitisation (MAR21.54–21.62) ─────────────────────────────────
CSR_NONSEC_RISK_WEIGHTS: Dict[str, float] = {
    # By credit quality / sector bucket
    "1":  0.005,   # Investment-grade (IG) sovereign
    "2":  0.010,   # IG local/regional government
    "3":  0.050,   # IG financial
    "4":  0.030,   # IG basic materials / energy
    "5":  0.030,   # IG consumer goods
    "6":  0.020,   # IG tech / telecoms
    "7":  0.025,   # IG healthcare / utilities
    "8":  0.015,   # IG covered bonds
    "9":  0.020,   # IG other
    "10": 0.030,   # High yield (HY) / non-rated (NR) sovereign
    "11": 0.050,   # HY/NR local/regional government
    "12": 0.070,   # HY/NR financial
    "13": 0.050,   # HY/NR basic materials / energy
    "14": 0.050,   # HY/NR consumer goods
    "15": 0.050,   # HY/NR tech / telecoms
    "16": 0.050,   # HY/NR healthcare / utilities
    "17": 0.120,   # HY/NR other
    "18": 0.150,   # Residual
}

CSR_NONSEC_CORRELATIONS: Dict[str, float] = {
    "rho_name":   0.35,   # same issuer, different tenor/seniority
    "rho_tenor":  0.65,   # same issuer, same tenor
    "rho_basis":  0.999,  # same bond, basis risk
    "gamma_bc":   0.35,
}

# ── FX (MAR21.88–21.91) ──────────────────────────────────────────────────────
FX_RISK_WEIGHTS: Dict[str, float] = {
    "default": 0.15,     # 15% for all FX pairs
    "pegged":  0.10,     # reduced for pegged/managed pairs (apply manually)
}

FX_CORRELATIONS: Dict[str, float] = {
    "gamma_bc": 0.60,
}

# ── Commodity (MAR21.81–21.87) ────────────────────────────────────────────────
COMMODITY_RISK_WEIGHTS: Dict[str, float] = {
    "1":  0.30,   # Energy – solid combustibles
    "2":  0.35,   # Energy – liquid combustibles
    "3":  0.60,   # Energy – electricity / carbon trading
    "4":  0.80,   # Freight
    "5":  0.40,   # Metals – non-precious
    "6":  0.20,   # Gaseous combustibles
    "7":  0.18,   # Precious metals (incl. gold)
    "8":  0.35,   # Grains / oilseed
    "9":  0.20,   # Livestock / dairy
    "10": 0.35,   # Softs / other agricultural
    "11": 0.50,   # Other commodities
}

COMMODITY_CORRELATIONS: Dict[str, float] = {
    "rho_same_grade": 0.70,
    "rho_diff_grade": 0.40,
    "gamma_bc":       0.20,
}

# ── CSR Securitisation (MAR21.63–21.70) ────────────────────────────────────
CSR_SEC_RISK_WEIGHTS: Dict[str, float] = {
    "1": 0.016,   # Senior IG
    "2": 0.025,   # Senior mezzanine
    "3": 0.050,   # Non-senior IG
    "4": 0.100,   # Non-senior HY
    "default": 0.030,
}

CSR_SEC_CORRELATIONS: Dict[str, float] = {
    "rho_intra": 0.40,
    "gamma_bc":  0.0,
}

# ── Master lookup ──────────────────────────────────────────────────────────────
RISK_WEIGHTS_BY_CLASS: Dict[str, Dict[str, float]] = {
    "GIRR":       GIRR_RISK_WEIGHTS,
    "Equity":     EQUITY_RISK_WEIGHTS,
    "CSR_NonSec": CSR_NONSEC_RISK_WEIGHTS,
    "CSR_Sec":    CSR_SEC_RISK_WEIGHTS,
    "FX":         FX_RISK_WEIGHTS,
    "Commodity":  COMMODITY_RISK_WEIGHTS,
}

CORRELATIONS_BY_CLASS: Dict[str, Dict[str, float]] = {
    "GIRR":       GIRR_CORRELATIONS,
    "Equity":     EQUITY_CORRELATIONS,
    "CSR_NonSec": CSR_NONSEC_CORRELATIONS,
    "CSR_Sec":    CSR_SEC_CORRELATIONS,
    "FX":         FX_CORRELATIONS,
    "Commodity":  COMMODITY_CORRELATIONS,
}

# ── Statutory default intra-bucket correlations (MAR21) ──────────────────────
# Used when specific pair-wise correlations are not defined between different names/grades.
DEFAULT_INTRA_CORRELATIONS: Dict[str, float] = {
    "GIRR":       0.80,   # MAR21.47 general yield curve baseline
    "Equity":     0.25,   # MAR21.76 different names in same bucket
    "CSR_NonSec": 0.35,   # MAR21.58 different issuers in same bucket
    "CSR_Sec":    0.40,   # MAR21.66 intra-bucket securitisation
    "Commodity":  0.40,   # MAR21.84 different commodity sub-grades
    "FX":         0.60,   # MAR21.90
}
