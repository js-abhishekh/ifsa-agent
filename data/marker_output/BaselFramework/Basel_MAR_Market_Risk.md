# Basel Framework — Market Risk (MAR / FRTB)


## MAR10 Market risk terminology ................................................................................. 728


## MAR10 .94 address the calculation of counterparty credit risk for SFTs

Market risk terminology
This chapter provides a high-level description of 
terminologies used in the market risk and credit 
valuation adjustment risk frameworks
Version effective as of
01 Jan 2023
Reflects revisions in the standardised and 
internal models approach for market risk, 
including the shift to an expected shortfall 
measure. Also reflects the revised 
implementation date announced on 27 March 
2020.
General terminology
Terminology for financial instruments
Terminology for market risk capital requirement calculations
Market risk: the risk of losses in on- and off-balance sheet risk positions arising 
from movements in market prices.
10.1
Notional value: the notional value of a derivative instrument is equal to the 
number of units underlying the instrument multiplied by the current market value 
of each unit of the underlying.

### MAR10.2 .94 address the calculation of counterparty credit risk for SFTs
10.2

Trading desk: a group of traders or trading accounts in a business line within a 
bank that follows defined trading strategies with the goal of generating revenues 
or maintaining market presence from assuming and managing risk.

### MAR10.3 .94 address the calculation of counterparty credit risk for SFTs
10.3

Pricing model: a model that is used to determine the value of an instrument 
(mark-to-market or mark-to-model) as a function of pricing parameters or to 
determine the change in the value of an instrument as a function of risk factors. A 
pricing model may be the combination of several calculations; eg a first valuation 
technique to compute a price, followed by valuation adjustments for risks that are 
not incorporated in the first step.

### MAR10.4 .94 address the calculation of counterparty credit risk for SFTs
10.4

Financial instrument: any contract that gives rise to both a financial asset of one 
entity and a financial liability or equity instrument of another entity. Financial 
instruments include both primary financial instruments (or cash instruments) and 
derivative financial instruments.

### MAR10.5 .94 address the calculation of counterparty credit risk for SFTs
10.5

Instrument: the term used to describe financial instruments, instruments on 
foreign exchange (FX) and commodities. 
10.6
Embedded derivative: a component of a financial instrument that includes a non-
derivative host contract. For example, the conversion option in a convertible 
bond is an embedded derivative.

### MAR10.7 .94 address the calculation of counterparty credit risk for SFTs
10.7

Look-through approach: an approach in which a bank determines the relevant 
capital requirements for a position that has underlyings (such as an index 
instrument, multi-underlying option, or an equity investment in a fund) as if the 
underlying positions were held directly by the bank.

### MAR10.8 .94 address the calculation of counterparty credit risk for SFTs
10.8

Risk factor: a principal determinant of the change in value of an instrument (eg an 
exchange rate or interest rate). 
10.9
Terminology for risk metrics
Risk position: the portion of the current value of an instrument that may be 
subject to losses due to movements in a risk factor. For example, a bond 
denominated in a currency different to a bank’s reporting currency has risk 
positions in general interest rate risk, credit spread risk (non-securitisation) and 
FX risk, where the risk positions are the potential losses to the current value of 
the instrument that could occur due to a change in the relevant underlying risk 
factors (interest rates, credit spreads, or exchange rates).

### MAR10.10 .94 address the calculation of counterparty credit risk for SFTs
10.10

Risk bucket: a defined group of risk factors with similar characteristics.
10.11
Risk class: a defined list of risks that are used as the basis for calculating market 
risk capital requirements: general interest rate risk, credit spread risk (non-
securitisation), credit spread risk (securitisation: non-correlation trading portfolio), 
credit spread risk (securitisation: correlation trading portfolio), FX risk, equity risk 
and commodity risk.

### MAR10.12 .94 address the calculation of counterparty credit risk for SFTs
10.12

Sensitivity: a bank’s estimate of the change in value of an instrument due to a 
small change in one of its underlying risk factors. Delta and vega risks are 
sensitivities.

### MAR10.13 .94 address the calculation of counterparty credit risk for SFTs
10.13

Delta risk: the linear estimate of the change in value of a financial instrument due 
to a movement in the value of a risk factor. The risk factor could be the price of 
an equity or commodity, or a change in an interest rate, credit spread or FX rate.

### MAR10.14 .94 address the calculation of counterparty credit risk for SFTs
10.14

Vega risk: the potential loss resulting from the change in value of a derivative due 
to a change in the implied volatility of its underlying.
10.15
Curvature risk: the additional potential loss beyond delta risk due to a change in a 
risk factor for financial instruments with optionality. In the standardised approach 
in the market risk framework, it is based on two stress scenarios involving an 
upward shock and a downward shock to each regulatory risk factor.

### MAR10.16 .94 address the calculation of counterparty credit risk for SFTs
10.16

Value at risk (VaR): a measure of the worst expected loss on a portfolio of 
instruments resulting from market movements over a given time horizon and a 
pre-defined confidence level.

### MAR10.17 .94 address the calculation of counterparty credit risk for SFTs
10.17

Expected shortfall (ES): a measure of the average of all potential losses exceeding 
the VaR at a given confidence level.
10.18
Jump-to-default (JTD): the risk of a sudden default. JTD exposure refers to the 
loss that could be incurred from a JTD event.
10.19
Terminology for hedging and diversification
Terminology for risk factor eligibility and modellability
Liquidity horizon: the time assumed to be required to exit or hedge a risk position 
without materially affecting market prices in stressed market conditions.

### MAR10.20 .94 address the calculation of counterparty credit risk for SFTs
10.20

Basis risk: the risk that prices of financial instruments in a hedging strategy are 
imperfectly correlated, reducing the effectiveness of the hedging strategy.
10.21
Diversification: the reduction in risk at a portfolio level due to holding risk 
positions in different instruments that are not perfectly correlated with one 
another.

### MAR10.22 .94 address the calculation of counterparty credit risk for SFTs
10.22

Hedge: the process of counterbalancing risks from exposures to long and short 
risk positions in correlated instruments.
10.23
Offset: the process of netting exposures to long and short risk positions in the 
same risk factor.
10.24
Standalone: being capitalised on a stand-alone basis means that risk positions are 
booked in a discrete, non-diversifiable trading book portfolio so that the risk 
associated with those risk positions cannot diversify, hedge or offset risk arising 
from other risk positions, nor be diversified, hedged or offset by them.

### MAR10.25 .94 address the calculation of counterparty credit risk for SFTs
10.25

Real prices: a term used for assessing whether risk factors pass the risk factor 
eligibility test. A price will be considered real if it is (i) a price from an actual 
transaction conducted by the bank, (ii) a price from an actual transaction between 
other arm’s length parties (eg at an exchange), or (iii) a price taken from a firm 
quote (ie a price at which the bank could transact with an arm’s length party).

### MAR10.26 .94 address the calculation of counterparty credit risk for SFTs
10.26

Modellable risk factor: risk factors that are deemed modellable, based on the 
number of representative real price observations and additional qualitative 
principles related to the data used for the calibration of the ES model. Risk factors 
that do not meet the requirements for the risk factor eligibility test are deemed 
as non-modellable risk factors (NMRF).

### MAR10.27 .94 address the calculation of counterparty credit risk for SFTs
10.27

Terminology for internal model validation
Terminology for credit valuation adjustment risk
Backtesting: the process of comparing daily actual and hypothetical profits and 
losses with model-generated VaR measures to assess the conservatism of risk 
measurement systems.

### MAR10.28 .94 address the calculation of counterparty credit risk for SFTs
10.28

Profit and loss (P&L) attribution (PLA): a method for assessing the robustness of 
banks’ risk management models by comparing the risk-theoretical P&L predicted 
by trading desk risk management models with the hypothetical P&L.

### MAR10.29 .94 address the calculation of counterparty credit risk for SFTs
10.29

Trading desk risk management model: the trading desk risk management model 
(pertaining to in-scope desks) includes all risk factors that are included in the 
bank’s ES model with supervisory parameters and any risk factors deemed not 
modellable, which are therefore not included in the ES model for calculating the 
respective regulatory capital requirement, but are included in NMRFs.

### MAR10.30 .94 address the calculation of counterparty credit risk for SFTs
10.30

Actual P&L (APL): the actual P&L derived from the daily P&L process. It includes 
intraday trading as well as time effects and new and modified deals, but excludes 
fees and commissions as well as valuation adjustments for which separate 
regulatory capital approaches have been otherwise specified as part of the rules 
or which are deducted from Common Equity Tier 1. Any other valuation 
adjustments that are market risk-related must be included in the APL. As is the 
case for the hypothetical P&L, the APL should include FX and commodity risks 
from positions held in the banking book.

### MAR10.31 .94 address the calculation of counterparty credit risk for SFTs
10.31

Hypothetical P&L (HPL): the daily P&L produced by revaluing the positions held 
at the end of the previous day using the market data at the end of the current 
day. Commissions, fees, intraday trading and new/modified deals, valuation 
adjustments for which separate regulatory capital approaches have been 
otherwise specified as part of the rules and valuation adjustments which are 
deducted from CET1 are excluded from the HPL. Valuation adjustments updated 
daily should usually be included in the HPL. Time effects should be treated in a 
consistent manner in the HPL and risk-theoretical P&L.

### MAR10.32 .94 address the calculation of counterparty credit risk for SFTs
10.32

Risk-theoretical P&L (RTPL): the daily desk-level P&L that is predicted by the 
valuation engines in the trading desk risk management model using all risk 
factors used in the trading desk risk management model (ie including the NMRFs).

### MAR10.33 .94 address the calculation of counterparty credit risk for SFTs
10.33

Credit valuation adjustment (CVA): an adjustment to the valuation of a derivative 
transaction to account for the credit risk of contracting parties.
10.34
CVA risk: the risk of changes to CVA arising from changes in credit spreads of the 
contracting parties, compounded by changes to the value or variability in the 
value of the underlying of the derivative transaction.

### MAR10.35 .94 address the calculation of counterparty credit risk for SFTs
10.35


## MAR11 .94 address the calculation of counterparty credit risk for SFTs

Definitions and application of 
market risk
This chapter defines the methods available for 
calculating and the scope of application of 
market risk capital requirements.
Version effective as of
01 Jan 2023
Definition and scope of application
Market risk is defined as the risk of losses arising from movements in market 
prices. The risks subject to market risk capital requirements include but are not 
limited to:

### MAR11.1 .94 address the calculation of counterparty credit risk for SFTs
11.1

(1)
default risk, interest rate risk, credit spread risk, equity risk, foreign exchange 
(FX) risk and commodities risk for trading book instruments; and
(2)
FX risk and commodities risk for banking book instruments.
All transactions, including forward sales and purchases, shall be included in the 
calculation of capital requirements as of the date on which they were entered 
into. Although regular reporting will in principle take place only at intervals 
(quarterly in most countries), banks are expected to manage their market risk in 
such a way that the capital requirements are being met on a continuous basis, 
including at the close of each business day. Supervisory authorities have at their 
disposal a number of effective measures to ensure that banks do not window-
dress by showing significantly lower market risk positions on reporting dates. 
Banks will also be expected to maintain strict risk management systems to ensure 
that intraday exposures are not excessive. If a bank fails to meet the capital 
requirements at any time, the national authority shall ensure that the bank takes 
immediate measures to rectify the situation.

### MAR11.2 .94 address the calculation of counterparty credit risk for SFTs
11.2

A matched currency risk position will protect a bank against loss from 
movements in exchange rates, but will not necessarily protect its capital 
adequacy ratio. If a bank has its capital denominated in its domestic currency and 
has a portfolio of foreign currency assets and liabilities that is completely 
matched, its capital/asset ratio will fall if the domestic currency depreciates. By 
running a short risk position in the domestic currency, the bank can protect its 
capital adequacy ratio, although the risk position would lead to a loss if the 
domestic currency were to appreciate. Supervisory authorities are free to allow 
banks to protect their capital adequacy ratio in this way and exclude certain 
currency risk positions from the calculation of net open currency risk positions, 
subject to meeting each of the following conditions:

### MAR11.3 .94 address the calculation of counterparty credit risk for SFTs
11.3

(1)
The risk position is taken or maintained for the purpose of hedging partially 
or totally against the potential that changes in exchange rates could have an 
adverse effect on its capital ratio.
(2)
The risk position is of a structural (ie non-dealing) nature such as positions 
stemming from:
(a)
investments in affiliated but not consolidated entities denominated in 
foreign currencies; or
(b)
investments in consolidated subsidiaries or branches denominated in 
foreign currencies.
(3)
The exclusion is limited to the amount of the risk position that neutralises 
the sensitivity of the capital ratio to movements in exchange rates.
(4)
The exclusion from the calculation is made for at least six months.
(5)
The establishment of a structural FX position and any changes in its position 
must follow the bank’s risk management policy for structural FX positions. 
This policy must be pre-approved by the national supervisor.
(6)
Any exclusion of the risk position needs to be applied consistently, with the 
exclusionary treatment of the hedge remaining in place for the life of the 
assets or other items.
(7)
The bank is subject to a requirement by the national supervisor to document 
and have available for supervisory review the positions and amounts to be 
excluded from market risk capital requirements.
No FX risk capital requirement need apply to positions related to items that are 
deducted from a bank’s capital when calculating its capital base.
11.4
Holdings of capital instruments that are deducted from a bank’s capital or risk 
weighted at 1250% are not allowed to be included in the market risk framework. 
This includes:

### MAR11.5 .94 address the calculation of counterparty credit risk for SFTs
11.5

(1)
holdings of the bank’s own eligible regulatory capital instruments; and
(2)
holdings of other banks’, securities firms’ and other financial entities’ eligible 
regulatory capital instruments, as well as intangible assets, where the 
national supervisor requires that such assets are deducted from capital.
(3)
Where a bank demonstrates that it is an active market-maker, then a 
national supervisor may establish a dealer exception for holdings of other 
banks’, securities firms’, and other financial entities’ capital instruments in the 
trading book. In order to qualify for the dealer exception, the bank must 
have adequate systems and controls surrounding the trading of financial 
institutions’ eligible regulatory capital instruments.
Footnotes
In the same way as for credit risk and operational risk, the capital requirements 
for market risk apply on a worldwide consolidated basis.

### MAR11.6 .94 address the calculation of counterparty credit risk for SFTs
11.6

(1)
Supervisory authorities may permit banking and financial entities in a group 
which is running a global consolidated trading book and whose capital is 
being assessed on a global basis to include just the net short and net long 
risk positions no matter where they are booked.1
(2)
Supervisory authorities may grant this treatment only when the standardised 
approach in 
 to 
 permits a full offset of the risk position (ie risk 
MAR20
MAR23
positions of the opposite sign do not attract a capital requirement).
(3)
Nonetheless, there will be circumstances in which supervisory authorities 
demand that the individual risk positions be taken into the measurement 
system without any offsetting or netting against risk positions in the 
remainder of the group. This may be needed, for example, where there are 
obstacles to the quick repatriation of profits from a foreign subsidiary or 
where there are legal and procedural difficulties in carrying out the timely 
management of risks on a consolidated basis.
(4)
Moreover, all supervisory authorities will retain the right to continue to 
monitor the market risks of individual entities on a non-consolidated basis to 
ensure that significant imbalances within a group do not escape supervision. 
Supervisory authorities will be especially vigilant in ensuring that banks do 
not conceal risk positions on reporting dates in such a way as to escape 
measurement.
The positions of less than wholly owned subsidiaries would be subject 
to the generally accepted accounting principles in the country where 
the parent company is supervised.
1
Methods of measuring market risk
In determining its market risk for regulatory capital requirements, a bank may 
choose between two broad methodologies: the standardised approach and 
internal models approach (IMA) for market risk, described in 
 to 
 
MAR20
MAR23
and 
 to 
, respectively, subject to the approval of the national 
MAR30
MAR33
authorities. Supervisors may allow banks that maintain smaller or simpler trading 
books to use the simplified alternative to the standardised approach as set out in
.
MAR40

### MAR11.7 .94 address the calculation of counterparty credit risk for SFTs
11.7

(1)
To determine the appropriateness of the simplified alternative for use by a 
bank for the purpose of its market risk capital requirements, supervisors may 
wish to consider the following indicative criteria:
(a)
The bank should not be a global systemically important bank (G-SIB).
(b)
The bank should not use the IMA for any of its trading desks.
(c)
The bank should not hold any correlation trading positions.
(2)
The use of the simplified alternative is subject to supervisory approval and 
oversight. Supervisors can mandate that banks with relatively complex or 
sizeable risks in particular risk classes apply the full standardised approach 
instead of the simplified alternative, even if those banks meet the indicative 
eligibility criteria referred to above.
All banks, except for those that are allowed to use the simplified alternative as set 
out in 
, must calculate the capital requirements using the standardised 
MAR11.7
approach. Banks that are approved by the supervisor to use the IMA for market 
risk capital requirements must also calculate and report the capital requirement 
values calculated as set out below.

### MAR11.8 .94 address the calculation of counterparty credit risk for SFTs
11.8

(1)
A bank that uses the IMA for any of its trading desks must also calculate the 
capital requirement under the standardised approach for all instruments 
across all trading desks, regardless of whether those trading desks are 
eligible for the IMA.
(2)
In addition, a bank that uses the IMA for any of its trading desks must 
calculate the standardised approach capital requirement for each trading 
desk that is eligible for the IMA as if that trading desk were a standalone 
regulatory portfolio (ie with no offsetting across trading desks). This will:
(a)
serve as an indication of the fallback capital requirement for those desks 
that fail the eligibility criteria for inclusion in the bank’s internal model 
as outlined in 
, 
 and 
; 
MAR30 MAR32
MAR33
(b)
generate information on the capital outcomes of the internal models 
relative to a consistent benchmark and facilitate comparison in 
implementation between banks and/or across jurisdictions;
(c)
monitor over time the relative calibration of standardised and modelled 
approaches, facilitating adjustments as needed; and
(d)
provide macroprudential insight in an ex ante consistent format.
All banks must calculate the market risk capital requirement using the 
standardised approach for the following:
11.9
(1)
securitisation exposures; and
(2)
equity investments in funds that cannot be looked through but are assigned 
to the trading book in accordance to the conditions set out in 
(5)(b).
RBC25.8

## MAR12 .94 address the calculation of counterparty credit risk for SFTs

Definition of trading desk
This chapter defines a trading desk, which is the 
level at which model approval is granted.
Version effective as of
01 Jan 2023
For the purposes of market risk capital calculations, a trading desk is a group of 
traders or trading accounts that implements a well defined business strategy 
operating within a clear risk management structure.

### MAR12.1 .94 address the calculation of counterparty credit risk for SFTs
12.1

Trading desks are defined by the bank but subject to the regulatory approval of 
the supervisor for capital purposes. 
12.2
(1)
A bank should be allowed to propose the trading desk structure per their 
organisational structure, consistent with the requirements set out in 
.
MAR12.4
(2)
A bank must prepare a policy document for each trading desk it defines, 
documenting how the bank satisfies the key elements in 
. 
MAR12.4
(3)
Supervisors will treat the definition of the trading desk as part of the initial 
model approval for the trading desk, as well as ongoing approval:
(a)
Supervisors may determine, based on the size of the bank’s overall 
trading operations, whether the proposed trading desk definitions are 
sufficiently granular.
(b)
Supervisors should check that the bank’s proposed definition of trading 
desk meets the criteria listed in key elements set out in 
.
MAR12.4
Within this supervisory approved trading desk structure, banks may further define 
operational subdesks without the need for supervisory approval. These subdesks 
would be for internal operational purposes only and would not be used in the 
market risk capital framework.

### MAR12.3 .94 address the calculation of counterparty credit risk for SFTs
12.3

The key attributes of a trading desk are as follows:
12.4
(1)
A trading desk for the purposes of the regulatory capital charge is an 
unambiguously defined group of traders or trading accounts.
(a)
A trading account is an indisputable and unambiguous unit of 
observation in accounting for trading activity.
(b)
The trading desk must have one head trader and can have up to two 
head traders provided their roles, responsibilities and authorities are 
either clearly separated or one has ultimate oversight over the other.
(i)
The head trader must have direct oversight of the group of traders 
or trading accounts.
(ii)
Each trader or each trading account in the trading desk must have a 
clearly defined specialty (or specialities).
(c)
Each trading account must only be assigned to a single trading desk. 
The desk must have a clearly defined risk scope consistent with its pre-
established objectives. The scope should include specification of the 
desk’s overall risk class and permitted risk factors.
(d)
There is a presumption that traders (as well as head traders) are 
allocated to one trading desk. A bank can deviate from this 
presumption and may assign an individual trader to work across several 
trading desks provided it can be justified to the supervisor on the basis 
of sound management, business and/or resource allocation reasons. 
Such assignments must not be made for the only purpose of avoiding 
other trading desk requirements (eg to optimise the likelihood of 
success in the backtesting and profit and loss attribution tests).
(e)
The trading desk must have a clear reporting line to bank senior 
management, and should have a clear and formal compensation policy 
clearly linked to the pre-established objectives of the trading desk.
(2)
A trading desk must have a well defined and documented business strategy, 
including an annual budget and regular management information reports 
(including revenue, costs and risk-weighted assets).
(a)
There must be a clear description of the economics of the business 
strategy for the trading desk, its primary activities and trading/hedging 
strategies.
(i)
Economics: what is the economics behind the strategy (eg trading 
on the shape of the yield curve)? How much of the activities are 
customer driven? Does it entail trade origination and structuring, 
or execution services, or both?
(ii)
Primary activities: what is the list of permissible instruments and, 
out of this list, which are the instruments most frequently traded?
(iii)
Trading/hedging strategies: how would these instruments be 
hedged, what are the expected slippages and mismatches of 
hedges, and what is the expected holding period for positions?
(b)
The management team at the trading desk (starting from the head 
trader) must have a clear annual plan for the budgeting and staffing of 
the trading desk.
(c)
A trading desk’s documented business strategy must include regular 
Management Information reports, covering revenue, costs and risk-
weighted assets for the trading desk.
(3)
A trading desk must have a clear risk management structure.
(a)
Risk management responsibilities: the bank must identify key groups 
and personnel responsible for overseeing the risk-taking activities at the 
trading desk.
(b)
A trading desk must clearly define trading limits based on the business 
strategy of the trading desk and these limits must be reviewed at least 
annually by senior management at the bank. In setting limits, the 
trading desk must have:
(i)
well defined trading limits or directional exposures at the trading 
desk level that are based on the appropriate market risk metric (eg 
sensitivity of credit spread risk and/or jump-to-default for a credit 
trading desk), or just overall notional limits; and
(ii)
well defined trader mandates.
(c)
A trading desk must produce, at least weekly, appropriate risk 
management reports. This would include, at a minimum:
profit and loss reports, which would be periodically reviewed, validated 
and modified (if necessary) by Product Control; and
internal and regulatory risk measure reports, including trading desk 
value-at-risk (VaR) / expected shortfall (ES), trading desk VaR/ES 
sensitivities to risk factors, backtesting and p-value.
The bank must prepare, evaluate, and have available for supervisors the following 
for all trading desks:
12.5
(1)
inventory ageing reports;
(2)
daily limit reports including exposures, limit breaches, and follow-up action;
(3)
reports on intraday limits and respective utilisation and breaches for banks 
with active intraday trading; and
(4)
reports on the assessment of market liquidity.
Any foreign exchange or commodity positions held in the banking book must be 
included in the market risk capital requirement as set out in 
. For 
MAR11.1
regulatory capital calculation purposes, these positions will be treated as if they 
were held on notional trading desks within the trading book.

### MAR12.6 .94 address the calculation of counterparty credit risk for SFTs
12.6

FAQ
How should the requirement for a “notional trading desk” be 
interpreted for banking book FX and commodities positions?
A “notional trading desk” is a trading desk that need not have traders 
or trading accounts assigned to it, and need not meet the qualitative 
trading desk requirements set out in 
.
MAR12
Banks that wish to use the internal models approach (IMA) to measure 
the FX or commodity risk of such “notional trading desks” must take 
either or both of the following actions:
-
transfer all or part of banking book FX and commodity risks to 
another trading desk via intra-trading book internal risk transfers 
(IRTs) (where trading desk requirements would continue to apply as 
appropriate for that desk), and/or
-
apply for IMA approval for the notional trading desk. In this case, 
the notional desk only needs to meet the quantitative trading desk 
requirements.
FAQ1
Does the standard permit certain traders (ie global treasury desk heads 
or department heads) to have ownership and responsibilities in both 
trading book and banking book portfolios?
Yes.
FAQ2

## MAR20 .94 address the calculation of counterparty credit risk for SFTs

Standardised approach: 
general provisions and 
structure
This chapter sets out the general provisions and 
the structure of the standardised approach for 
calculating risk-weighted assets for market risk.
Version effective as of
01 Jan 2023
Introduces a revised approach based on 
expanded use of sensitivities as set out in the 
January 2019 market risk publication and 
updated to take account of the revised 
implementation date announced on 27 March 
2020.
General provisions
Structure of the standardised approach
The risk-weighted assets for market risk under the standardised approach are 
determined by multiplying the capital requirements calculated as set out in
to 
 by 12.5.
MAR20
MAR23

### MAR20.1 .94 address the calculation of counterparty credit risk for SFTs
20.1

The standardised approach must be calculated and reported to the relevant 
supervisor on a monthly basis. Subject to supervisory approval, the standardised 
approach for market risks arising from non-banking subsidiaries of a bank may 
be calculated and reported to the relevant supervisor on a quarterly basis.

### MAR20.2 .94 address the calculation of counterparty credit risk for SFTs
20.2

A bank must also determine its regulatory capital requirements for market risk 
according to the standardised approach for market risk at the demand of its 
supervisor.

### MAR20.3 .94 address the calculation of counterparty credit risk for SFTs
20.3

The standardised approach capital requirement is the simple sum of three 
components: the capital requirement under the sensitivities-based method, the 
default risk capital (DRC) requirement and the residual risk add-on (RRAO).

### MAR20.4 .94 address the calculation of counterparty credit risk for SFTs
20.4

(1)
The capital requirement under the sensitivities-based method must be 
calculated by aggregating three risk measures - delta, vega and curvature, as 
set out in 
:
MAR21
(a)
: a risk measure based on sensitivities of an instrument to 
Delta
regulatory delta risk factors.
(b)
: a risk measure based on sensitivities to regulatory vega risk 
Vega
factors.
(c)
: a risk measure which captures the incremental risk not 
Curvature
captured by the delta risk measure for price changes in an option. 
Curvature risk is based on two stress scenarios involving an upward 
shock and a downward shock to each regulatory risk factor.
(d)
The above three risk measures specify risk weights to be applied to the 
regulatory risk factor sensitivities. To calculate the overall capital 
requirement, the risk-weighted sensitivities are aggregated using 
specified correlation parameters to recognise diversification benefits 
between risk factors. In order to address the risk that correlations may 
increase or decrease in periods of financial stress, a bank must calculate
three sensitivities-based method capital requirement values, based on 
three different scenarios on the specified values for the correlation 
parameters as set out in 
 and 
.
MAR21.6
MAR21.7
(2)
The DRC requirement captures the jump-to-default risk for instruments 
subject to credit risk as set out in 
. It is calibrated based on the 
MAR22.2
credit risk treatment in the banking book in order to reduce the potential 
discrepancy in capital requirements for similar risk exposures across the 
bank. Some hedging recognition is allowed for similar types of exposures 
(corporates, sovereigns, and local governments/municipalities).
(3)
Additionally, the Committee acknowledges that not all market risks can be 
captured in the standardised approach, as this might necessitate an unduly 
complex regime. An RRAO is thus introduced to ensure sufficient coverage 
of market risks for instruments specified in 
. The calculation method 
MAR23.2
for the RRAO is set out in 
.
MAR23.8
Definition of correlation trading portfolio
Footnotes
For the purpose of calculating the credit spread risk capital requirement under 
the sensitivities based method and the DRC requirement, the correlation trading 
portfolio is defined as the set of instruments that meet the requirements of (1) or 
(2) below.

### MAR20.5 .94 address the calculation of counterparty credit risk for SFTs
20.5

(1)
The instrument is a securitisation position that meets the following 
requirements:
(a)
The instrument is not a re-securitisation position, nor a derivative of 
securitisation exposures that does not provide a pro rata share in the 
proceeds of a securitisation tranche, where the definition of 
securitisation positon is identical to that used in the credit risk 
framework.
(b)
All reference entities are single-name products, including single-name 
credit derivatives, for which a liquid two-way market exists,1 including 
traded indices on these reference entities.
(c)
The instrument does not reference an underlying that is treated as a 
retail exposure, a residential mortgage exposure, or a commercial 
mortgage exposure under the standardised approach to credit risk.
(d)
The instrument does not reference a claim on a special purpose entity.
(2)
The instrument is a non-securitisation hedge to a position described above.
A two-way market is deemed to exist where there are independent 
bona fide offers to buy and sell so that a price reasonably related to the 
last sales price or current bona fide competitive bid-ask quotes can be 
determined within one day and the transaction settled at such price 
within a relatively short time frame in conformity with trade custom.
1

## MAR21 .94 address the calculation of counterparty credit risk for SFTs

Standardised approach: 
sensitivities-based method
This chapter sets out the calculation of the 
sensitivities-based method under the 
standardised approach for market risk.
Version effective as of
01 Jan 2023
Updated to take account of the revised 
implementation date announced on 27 March 
2020, and to incorporate the FAQs published on 
5 July 2024 and 23 March 2026.
Main concepts of the sensitivities-based method
The sensitivities of financial instruments to a prescribed list of risk factors are 
used to calculate the delta, vega and curvature risk capital requirements. These 
sensitivities are risk-weighted and then aggregated, first within risk buckets (risk 
factors with common characteristics) and then across buckets within the same 
risk class as set out in 
 to 
. The following terminology is used 
MAR21.8
MAR21.14
in the sensitivities-based method:

### MAR21.1 .94 address the calculation of counterparty credit risk for SFTs
21.1

(1)
Risk class: seven risk classes are defined (in 
 to 
).
MAR21.39
MAR21.89
(a)
General interest rate risk (GIRR)
(b)
Credit spread risk (CSR): non-securitisations
(c)
CSR: securitisations (non-correlation trading portfolio, or non-CTP)
(d)
CSR: securitisations (correlation trading portfolio, or CTP)
(e)
Equity risk
(f)
Commodity risk
(g)
Foreign exchange (FX) risk
(2)
Risk factor: variables (eg an equity price or a tenor of an interest rate curve) 
that affect the value of an instrument as defined in 
 to 
.
MAR21.8
MAR21.14
(3)
Bucket: a set of risk factors that are grouped together by common 
characteristics (eg all tenors of interest rate curves for the same currency), as 
defined in 
 to 
.
MAR21.39
MAR21.89
(4)
Risk position: the portion of the risk of an instrument that relates to a risk 
factor. Methodologies to calculate risk positions for delta, vega and 
curvature risks are set out in 
 to 
 and 
 to 
MAR21.3
MAR21.5
MAR21.15
MAR21.
. 
26
(a)
For delta and vega risks, the risk position is a sensitivity to a risk factor.
(b)
For curvature risk, the risk position is based on losses from two stress 
scenarios.
(5)
Risk capital requirement: the amount of capital that a bank should hold as a 
consequence of the risks it takes; it is computed as an aggregation of risk 
positions first at the bucket level, and then across buckets within a risk class 
defined for the sensitivities-based method as set out in 
 to 
.
MAR21.3
MAR21.7
Instruments subject to each component of the sensitivities-based 
method
In applying the sensitivities-based method, all instruments held in trading desks 
as set out in 
 and subject to the sensitivities-based method (ie excluding 
MAR12
instruments where the value at any point in time is purely driven by an exotic 
underlying as set out in 
), are subject to delta risk capital requirements. 
MAR23.3
Additionally, the instruments specified in (1) to (4) are subject to vega and 
curvature risk capital requirements:

### MAR21.2 .94 address the calculation of counterparty credit risk for SFTs
21.2

(1)
Any instrument with optionality.1
(2)
Any instrument with an embedded prepayment option2 – this is considered 
an instrument with optionality according to above (1). The embedded option 
is subject to vega and curvature risk with respect to interest rate risk and CSR 
(non-securitisation and securitisation) risk classes. When the prepayment 
option is a behavioural option the instrument may also be subject to the 
residual risk add-on (RRAO) as per 
. The pricing model of the bank 
MAR23
must reflect such behavioural patterns where relevant. For securitisation 
tranches, instruments in the securitised portfolio may have embedded 
prepayment options as well. In this case the securitisation tranche may be 
subject to the RRAO.
(3)
Instruments whose cash flows cannot be written as a linear function of 
underlying notional. For example, the cash flows generated by a plain-vanilla 
option cannot be written as a linear function (as they are the maximum of 
the spot and the strike). Therefore, all options are subject to vega risk and 
curvature risk. Instruments whose cash flows can be written as a linear 
function of underlying notional are instruments without optionality (eg cash 
flows generated by a coupon bearing bond can be written as a linear 
function) and are not subject to vega risk nor curvature risk capital 
requirements.
(4)
Curvature risks may be calculated for all instruments subject to delta risk, not 
limited to those subject to vega risk as specified in (1) to (3) above. For 
example, where a bank manages the non-linear risk of instruments with 
optionality and other instruments holistically, the bank may choose to 
include instruments without optionality in the calculation of curvature risk. 
This treatment is allowed subject to all of the following restrictions:
(a)
Use of this approach shall be applied consistently through time.
(b)
Curvature risk must be calculated for all instruments subject to the 
sensitivities-based method.
Footnotes
Process to calculate the capital requirement under the sensitivities-
based method
Calculation of the delta and vega risk capital requirement for each risk class
For example, each instrument that is an option or that includes an 
option (eg an embedded option such as convertibility or rate 
dependent prepayment and that is subject to the capital requirements 
for market risk). A non-exhaustive list of example instruments with 
optionality includes: calls, puts, caps, floors, swaptions, barrier options 
and exotic options.
1
An instrument with a prepayment option is a debt instrument which 
grants the debtor the right to repay part of or the entire principal 
amount before the contractual maturity without having to compensate 
for any foregone interest. The debtor can exercise this option with a 
financial gain to obtain funding over the remaining maturity of the 
instrument at a lower rate in other ways in the market.
2
As set out in 
, the capital requirement under the sensitivities-based 
MAR21.1
method is calculated by aggregating delta, vega and curvature capital 
requirements. The relevant paragraphs that describe this process are as follows:

### MAR21.3 .94 address the calculation of counterparty credit risk for SFTs
21.3

(1)
The risk factors for delta, vega and curvature risks for each risk class are 
defined in 
 to 
.
MAR21.8
MAR21.14
(2)
The methods to risk weight sensitivities to risk factors and aggregate them 
to calculate delta and vega risk positions for each risk class are set out in
and 
 to 
, which include the definition of delta 
MAR21.4
MAR21.15
MAR21.95
and vega sensitivities, definition of buckets, risk weights to apply to risk 
factors, and correlation parameters.
(3)
The methods to calculate curvature risk are set out in 
 and 
MAR21.5
MAR21.
 to 
, which include the definition of buckets, risk weights and 
96
MAR21.101
correlation parameters.
(4)
The risk class level capital requirement calculated above must be aggregated 
to obtain the capital requirement at the entire portfolio level as set out in
and 
.
MAR21.6
MAR21.7
For each risk class, a bank must determine its instruments’ sensitivity to a set of 
prescribed risk factors, risk weight those sensitivities, and aggregate the resulting 
risk-weighted sensitivities separately for delta and vega risk using the following 
step-by-step approach:

### MAR21.4 .94 address the calculation of counterparty credit risk for SFTs
21.4

(1)
For each risk factor (as defined in 
 to 
), a sensitivity is 
MAR21.8
MAR21.14
determined as set out in 
 to 
.
MAR21.15
MAR21.38
(2)
Sensitivities to the same risk factor must be netted to give a net sensitivity s 
k
across all instruments in the portfolio to each risk factor k. In calculating the 
net sensitivity, all sensitivities to the same given risk factor (eg all sensitivities 
to the one-year tenor point of the three-month Euribor swap curve) from 
instruments of opposite direction should offset, irrespective of the 
instrument from which they derive. For instance, if a bank’s portfolio is made 
of two interest rate swaps on three-month Euribor with the same fixed rate 
and same notional but of opposite direction, the GIRR on that portfolio 
would be zero.
(3)
The weighted sensitivity WS is the product of the net sensitivity s and the 
k
k
corresponding risk weight RW as defined in 
 to 
.
k
MAR21.39
MAR21.95
(4)
Within bucket aggregation: the risk position for delta (respectively vega) 
bucket b, K , must be determined by aggregating the weighted sensitivities 
b
to risk factors within the same bucket using the prescribed correlation
 set
out in the following formula, where the quantity within the square root 
function is floored at zero:
Calculation of the curvature risk capital requirement for each risk class
(5)
Across bucket aggregation: The delta (respectively vega) risk capital 
requirement is calculated by aggregating the risk positions across the delta 
(respectively vega) buckets within each risk class, using the corresponding
prescribed correlations
 as set out in the following formula, where:
(a)
 for all risk factors in bucket b, and
 in bucket c.
(b)
If these values for
 and
 described in above 
(5)(a) produce 
MAR21.4
a negative number for the overall sum of
 , the
bank is to calculate the delta (respectively vega) risk capital requirement 
using an alternative specification whereby:
(i)
 for all risk factors in bucket b; and
(ii)
 for all risk factors in bucket c.
For each risk class, to calculate curvature risk capital requirements a bank must 
apply an upward shock and a downward shock to each prescribed risk factor and 
calculate the incremental loss for instruments sensitive to that risk factor above 
that already captured by the delta risk capital requirement using the following 
step-by-step approach:

### MAR21.5 .94 address the calculation of counterparty credit risk for SFTs
21.5

(1)
For each instrument sensitive to curvature risk factor k, an upward shock and 
a downward shock must be applied to k. The size of shock (ie risk weight) is 
set out in 
 and 
.
MAR21.98
MAR21.99
(a)
For example for GIRR, all tenors of all the risk free interest rate curves 
within a given currency (eg three-month Euribor, six-month Euribor, one 
year Euribor, etc for the euro) must be shifted upward applying the risk 
weight as set out in 
. The resulting potential loss for each 
MAR21.99
instrument, after the deduction of the delta risk positions, is the 
outcome of the upward scenario. The same approach must be followed 
on a downward scenario.
(b)
If the price of an instrument depends on several risk factors, the 
curvature risk must be determined separately for each risk factor.
(2)
The net curvature risk capital requirement, determined by the values
and
 for a bank's portfolio for risk factor k described in above MAR21.5
(1) is calculated by the formula below. It calculates the aggregate 
incremental loss beyond the delta capital requirement for the prescribed 
shocks, where
(a)
i is an instrument subject to curvature risks associated with risk factor k;
(b)
 is the current level of risk factor k;
(c)
 is the price of instrument i at the current level of risk factor k;
(d)
 and
 denote the price of instrument i
after
 is shifted (ie "shocked") upward and downward respectively;
(e)
 is the risk weight for curvature risk factor k for instrument i;
and
(f)
 is the delta sensitivity of instrument i with respect to the delta risk
factor that corresponds to curvature risk factor k, where:
(i)
for the FX and equity risk classes,
 is the delta sensitivity of
instrument i; and
(ii)
for the GIRR, CSR and commodity risk classes,
 is the sum of delta
sensitivities to all tenors of the relevant curve of instrument i with 
respect to curvature risk factor k.
(3)
Within bucket aggregation: the curvature risk exposure must be aggregated
within each bucket using the corresponding prescribed correlation
 as set
out in the following formula, where:
(a)
The bucket level capital requirement (
 ) is determined as the greater of
the capital requirement under the upward scenario (
 ) and the capital
requirement under the downward scenario (
 ). Notably, the selection of
upward and downward scenarios is not necessarily the same across the 
high, medium and low correlations scenarios specified in 
.
MAR21.6
(i)
Where
 , this shall be termed "selecting the upward scenario".
(ii)
Where
 , this shall be termed "selecting the downward
scenario".
(iii)
In the specific case where
 if
 , it is
deemed that the upward scenario is selected; otherwise the 
downward scenario is selected.
(b)
 takes the value 0 if
 and
 both have negative
signs and the value 1 otherwise.
(4)
Across bucket aggregation: curvature risk positions must then be 
aggregated across buckets within each risk class, using the corresponding
prescribed correlations
 , where:
(a)
 for all risk factors in bucket b, when the upward scenario
has been selected for bucket b in above (3)(a).
 otherwise;
and
(b)
 takes the value 0 if
 and
 both have negative signs and 1
otherwise.
FAQ
When the delta effect is removed in the calculation of the curvature 
risk capital requirement, should the delta used in that calculation be 
the same as the delta used in the delta risk capital requirement? 
Should the same assumptions that go into the calculation of the delta 
(ie sticky delta for normal or log-normal volatilities) go into the 
calculation of the shifted or shocked price of the instrument?
The delta used for the calculation of the curvature risk capital 
requirement should be the same as that used for calculating the delta 
risk capital requirement. The assumptions that are used for the 
calculation of the delta (ie sticky delta for normal or log-normal 
volatilities) should also be used for calculating the shifted or shocked 
price of the instrument.
FAQ1
Are banks permitted to choose between zero rate and market rate 
sensitivities for GIRR delta and curvature capital requirements?
states that banks must determine each delta sensitivity, 
MAR21.17
vega sensitivity and curvature scenario based on instrument prices or 
pricing models that an independent risk control unit within a bank uses 
to report market risks or actual profits and losses to senior 
management. Banks should use zero rate or market rate sensitivities 
consistent with the pricing models referenced in that paragraph.
FAQ2
Calculation of aggregate sensitivities-based method capital requirement
In order to address the risk that correlations increase or decrease in periods of 
financial stress, the aggregation of bucket level capital requirements and risk 
class level capital requirements per each risk class for delta, vega, and curvature 
risks as specified in 
 to 
 must be repeated, corresponding to 
MAR21.4
MAR21.5
three different scenarios on the specified values for the correlation parameter
(correlation between risk factors within a bucket) and
 (correlation across
buckets within a risk class).

### MAR21.6 .94 address the calculation of counterparty credit risk for SFTs
21.6

(1)
Under the “medium correlations” scenario, the correlation parameters
 and
as specified in 
 to 
 apply.
MAR21.39
MAR21.101
(2)
Under the “high correlations” scenario, the correlation parameters
 and
that are specified in 
 to 
 are uniformly multiplied by 
MAR21.39
MAR21.101
1.25, with
 and
 subject to a cap at 100%.
(3)
Under the “low correlations” scenario, the correlation parameters
 and
that are specified in 
 to 
 are replaced by
MAR21.39
MAR21.101
and
.
The total capital requirement under the sensitivities-based method is aggregated 
as follows:
21.7
(1)
For each of three correlation scenarios, the bank must simply sum up the 
separately calculated delta, vega and curvature capital requirements for all 
risk classes to determine the overall capital requirement for that scenario.
Sensitivities-based method: risk factor and sensitivity definitions
Risk factor definitions for delta, vega and curvature risks
(2)
The sensitivities-based method capital requirement is the largest capital 
requirement from the three scenarios.
(a)
For the calculation of capital requirements for all instruments in all 
trading desks using the standardised approach as set out in 
(1) 
MAR11.8
and 
 and 
, the capital requirement is calculated for all 
MAR20.2
MAR33.40
instruments in all trading desks.
(b)
For the calculation of capital requirements for each trading desk using 
the standardised approach as if that desk were a standalone regulatory
portfolio as set out in 
(2), the capital requirements under each 
MAR11.8
correlation scenario are calculated and compared at each trading desk 
level, and the maximum for each trading desk is taken as the capital 
requirement.
GIRR factors
21.8
(1)
Delta GIRR: the GIRR delta risk factors are defined along two dimensions: (i) a 
risk-free yield curve for each currency in which interest rate-sensitive 
instruments are denominated and (ii) the following tenors: 0.25 years, 0.5 
years, 1 year, 2 years, 3 years, 5 years, 10 years, 15 years, 20 years and 30 
years, to which delta risk factors are assigned.3
(a)
The risk-free yield curve per currency should be constructed using 
money market instruments held in the trading book that have the 
lowest credit risk, such as overnight index swaps (OIS). Alternatively, the 
risk-free yield curve should be based on one or more market-implied 
swap curves used by the bank to mark positions to market. For example, 
interbank offered rate (BOR) swap curves.
(b)
When data on market-implied swap curves described in above (1)(a) are 
insufficient, the risk-free yield curve may be derived from the most 
appropriate sovereign bond curve for a given currency. In such cases 
the sensitivities related to sovereign bonds are not exempt from the 
CSR capital requirement: when a bank cannot perform the 
decomposition y=r+cs, any sensitivity to y is allocated both to the GIRR 
and to CSR classes as appropriate with the risk factor and sensitivity 
definitions in the standardised approach. Applying swap curves to bond-
derived sensitivities for GIRR will not change the requirement for basis 
risk to be captured between bond and credit default swap (CDS) curves 
in the CSR class.
(c)
For the purpose of constructing the risk-free yield curve per currency, an 
OIS curve (such as Eonia or a new benchmark rate) and a BOR swap 
curve (such as three-month Euribor or other benchmark rates) must be 
considered two different curves. Two BOR curves at different maturities 
(eg three-month Euribor and six-month Euribor) must be considered 
two different curves. An onshore and an offshore currency curve (eg 
onshore Indian rupee and offshore Indian rupee) must be considered 
two different curves.
(2)
The GIRR delta risk factors also include a flat curve of market-implied 
inflation rates for each currency with term structure not recognised as a risk 
factor.
(a)
The sensitivity to the inflation rate from the exposure to implied 
coupons in an inflation instrument gives rise to a specific capital 
requirement. All inflation risks for a currency must be aggregated to one 
number via simple sum.
(b)
This risk factor is only relevant for an instrument when a cash flow is 
functionally dependent on a measure of inflation (eg the notional 
amount or an interest payment depending on a consumer price index). 
GIRR risk factors other than for inflation risk will apply to such an 
instrument notwithstanding.
(c)
Inflation rate risk is considered in addition to the sensitivity to interest 
rates from the same instrument, which must be allocated, according to 
the GIRR framework, in the term structure of the relevant risk-free yield 
curve in the same currency.
(3)
The GIRR delta risk factors also include one of two possible cross-currency 
basis risk factors4 for each currency (ie each GIRR bucket) with the term 
structure not recognised as a risk factor (ie both cross-currency basis curves 
are flat).
(a)
The two cross-currency basis risk factors are basis of each currency over 
USD or basis of each currency over EUR. For instance, an AUD-
denominated bank trading a JPY/USD cross-currency basis swap would 
have a sensitivity to the JPY/USD basis but not to the JPY/EUR basis.
(b)
Cross-currency bases that do not relate to either basis over USD or basis 
over EUR must be computed either on "basis over USD" or "basis over 
EUR" but not both. GIRR risk factors other than for cross-currency basis 
risk will apply to such an instrument notwithstanding.
(c)
Cross-currency basis risk is considered in addition to the sensitivity to 
interest rates from the same instrument, which must be allocated, 
according to the GIRR framework, in the term structure of the relevant 
risk-free yield curve in the same currency.
(4)
Vega GIRR: within each currency, the GIRR vega risk factors are the implied 
volatilities of options that reference GIRR-sensitive underlyings; as defined 
along two dimensions:5
(a)
The maturity of the option: the implied volatility of the option as 
mapped to one or several of the following maturity tenors: 0.5 years, 1 
year, 3 years, 5 years and 10 years.
(b)
The residual maturity of the underlying of the option at the expiry date 
of the option: the implied volatility of the option as mapped to two (or 
one) of the following residual maturity tenors: 0.5 years, 1 year, 3 years, 
5 years and 10 years.
(5)
Curvature GIRR:
(a)
The GIRR curvature risk factors are defined along only one dimension: 
the constructed risk-free yield curve per currency with no term structure 
decomposition. For example, the euro, Eonia, three-month Euribor and 
six-month Euribor curves must be shifted at the same time in order to 
compute the euro-relevant risk-free yield curve curvature risk capital 
requirement. For the calculation of sensitivities, all tenors (as defined for 
delta GIRR) are to be shifted in parallel.
(b)
There is no curvature risk capital requirement for inflation and cross-
currency basis risks.
(6)
The treatment described in above (1)(b) for delta GIRR also applies to vega 
GIRR and curvature GIRR risk factors.
Footnotes
The assignment of risk factors to the specified tenors should be 
performed by linear interpolation or a method that is most consistent 
with the pricing functions used by the independent risk control function 
of a bank to report market risks or P&L to senior management.
3
Cross-currency basis are basis added to a yield curve in order to 
evaluate a swap for which the two legs are paid in two different 
currencies. They are in particular used by market participants to price 
cross-currency interest rate swaps paying a fixed or a floating leg in 
one currency, receiving a fixed or a floating leg in a second currency, 
and including an exchange of the notional in the two currencies at the 
start date and at the end date of the swap.
4
For example, an option with a forward starting cap, lasting 12 months, 
consists of four consecutive caplets on USD three-month Libor. There 
are four (independent) options, with option expiry dates in 12, 15, 18 
and 21 months. These options are all on underlying USD three-month 
Libor; the underlying always matures three months after the option 
expiry date (its residual maturity being three months). Therefore, the 
implied volatilities for a regular forward starting cap, which would start 
in one year and last for 12 months should be defined along the 
following two dimensions: (i) the maturity of the option’s individual 
components (caplets) – 12, 15, 18 and 21 months; and (ii) the residual 
maturity of the underlying of the option – three months.
5
FAQ
Different results can be produced depending on the bank’s curve 
methodology as diversification will be different for different 
methodologies. For example, if three-month Euribor is constructed as a 
“spread to EONIA”, this curve will be a spread curve and can be 
considered a different yield curve for the purpose of computing risk-
weighted PV01 and subsequent diversification. In this example, should 
three-month Euribor and EONIA be considered two distinct yield curves 
for the purpose of computing the risk capital requirement?
(1)(c)states that for the purpose of constructing the risk-free 
MAR21.8
yield curve per currency, an overnight index swap curve (such as 
EONIA) and an interbank offered rate curve (such as three-month 
Euribor) must be considered two different curves, with distinct risk 
factors in each tenor bucket, for the purpose of computing the risk 
capital requirement.
FAQ1
For GIRR, CSR, equity risk, commodity risk or FX risk, risk factors need 
to be assigned to prescribed tenors. How should this assignment be 
performed if the internally used tenors do not match the prescribed 
ones?
Banks are not permitted to perform capital computations based on 
internally used tenors. Risk factors and sensitivities must be assigned to 
the prescribed tenors. As stated in footnote 3 to 
 and footnote 
MAR21.8
8 to 
, the assignment of risk factors and sensitivities to the 
MAR21.25
specified tenors should be performed by linear interpolation or a 
method that is most consistent with the pricing functions used by the 
independent risk control function of the bank to report market risks or 
profits and losses to senior management.
FAQ2
When calculating the cross-currency basis spread (CCBS) capital 
requirement: since pricing models use a term structure-based CCBS 
curve, is it acceptable to use sensitivities to individual tenors 
aggregated by simple sum rather than explicitly modelling the CCBS 
curve as flat in the pricing model?
Yes. Banks may use a term structure-based CCBS curve and aggregate 
sensitivities to individual tenors by simple sum.
FAQ3
Should inflation and cross-currency bases be included as a risk factor 
in the vega GIRR capital requirement?
Yes. Inflation and cross-currency bases are included in the GIRR vega 
risk capital requirement. As no maturity dimension is specified for the 
delta capital requirement for inflation or cross-currency bases (ie the 
possible underlying of the option), the vega risk for inflation and cross-
currency bases should be considered only along the single dimension 
of the maturity of the option.
FAQ4
Should a bank compute delta, vega and curvature risk for callable 
bonds, options on sovereign bond futures and bond options?
For the specified instruments, delta, vega and curvature capital 
requirements must be computed for both GIRR and CSR.
FAQ5
The sensitivities-based approach defines the repo risk factor only in the 
context of equities and not for fixed income funding instruments (to the 
extent that these instruments fall within the trading book definition as 
trading-related repo-style transactions). Is it the intention that fixed 
income funding instruments be excluded from the equity repo 
treatment? If so, should such funding instruments be subject to the
FAQ6
GIRR capital requirement – for example, by considering the repo curve 
for a given currency as a yield curve subject to interest rate shocks?
Repo rate risk factors for fixed income funding instruments are subject 
to the GIRR capital requirement. A relevant repo curve should be 
considered by currency.
May risk weights be floored for interest rates when applying the risk 
weights for GIRR, given that there is a possibility of the interest rates 
being negative (eg for JPY and EUR curves)?
No such floor is permitted in the market risk standard for GIRR.
FAQ7
CSR non-securitisation risk factors
21.9
(1)
Delta CSR non-securitisation: the CSR non-securitisation delta risk factors are 
defined along two dimensions:
(a)
the relevant issuer credit spread curves (bond and CDS); and
(b)
the following tenors: 0.5 years, 1 year, 3 years, 5 years and 10 years.
(2)
Vega CSR non-securitisation: the vega risk factors are the implied volatilities 
of options that reference the relevant credit issuer names as underlyings 
(bond and CDS); further defined along one dimension - the maturity of the 
option. This is defined as the implied volatility of the option as mapped to 
one or several of the following maturity tenors: 0.5 years, 1 year, 3 years, 5 
years and 10 years.
(3)
Curvature CSR non-securitisation: the CSR non-securitisation curvature risk 
factors are defined along one dimension: the relevant issuer credit spread 
curves (bond and CDS). For instance, the bond-inferred spread curve of an 
issuer and the CDS-inferred spread curve of that same issuer should be 
considered a single spread curve. For the calculation of sensitivities, all 
tenors (as defined for CSR) are to be shifted in parallel.
FAQ
The second FAQ under 
 is also relevant to this paragraph.
MAR21.8
FAQ1
Should a bank compute delta, vega and curvature risk for callable 
bonds, options on sovereign bond futures and bond options?
For the specified instruments, delta, vega and curvature capital 
requirements must be computed for both GIRR and CSR.
FAQ2
(3) explicitly states that, for CSR curvature, the bond-CDS 
MAR21.9
basis is ignored. Is it correct that, under 
(1), bond and CDS 
MAR21.9
curves are considered distinct risk factors and the only “basis” taken
into account in
in 
 and 
 is the bond-CDS 
 
 
MAR21.54
MAR21.55
basis?
Yes. Bond and CDS credit spreads are considered distinct risk factors
under 
(1), and
referenced in 
 and 
 
MAR21.9
 
 
MAR21.54
MAR21.55
is meant to capture only the bond-CDS basis.
FAQ3
May risk weights be floored for credit spreads when applying the risk 
weights for the CSR risk classes?
No such floor is permitted in the market risk standard for the CSR risk 
classes, except for CSR curvature under the conditions set out in the 
second FAQ under 
.
MAR21.99
FAQ4
CSR securitisation: non-CTP risk factors
21.10
(1)
For securitisation instruments that do not meet the definition of CTP as set 
out in 
 (ie, non-CTP), the sensitivities of delta risk factors (ie CS01) 
MAR20.5
must be calculated with respect to the spread of the tranche rather than the 
spread of the underlying of the instruments.
(2)
Delta CSR securitisation (non-CTP): the CSR securitisation delta risk factors 
are defined along two dimensions:
(a)
Tranche credit spread curves; and
(b)
The following tenors: 0.5 years, 1 year, 3 years, 5 years and 10 years to 
which delta risk factors are assigned.
(3)
Vega CSR securitisation (non-CTP): Vega risk factors are the implied 
volatilities of options that reference non-CTP credit spreads as underlyings 
(bond and CDS); further defined along one dimension - the maturity of the 
option. This is defined as the implied volatility of the option as mapped to 
one or several of the following maturity tenors: 0.5 years, 1 year, 3 years, 5 
years and 10 years.
(4)
Curvature CSR securitisation (non-CTP): the CSR securitisation curvature risk 
factors are defined along one dimension, the relevant tranche credit spread 
curves (bond and CDS). For instance, the bond-inferred spread curve of a 
given Spanish residential mortgage-backed security (RMBS) tranche and the
CDS-inferred spread curve of that given Spanish RMBS tranche would be 
considered a single spread curve. For the calculation of sensitivities, all the 
tenors are to be shifted in parallel.
FAQ
The second FAQ under 
 is also relevant to this paragraph.
MAR21.8
FAQ1
May risk weights be floored for credit spreads when applying the risk 
weights for the CSR risk classes?
No such floor is permitted in the market risk standard for the CSR risk 
classes, except for CSR curvature under the conditions set out in the 
second FAQ under 
.
MAR21.99
FAQ2
CSR securitisation: CTP risk factors
21.11
(1)
For securitisation instruments that meet the definition of a CTP as set out in
, the sensitivities of delta risk factors (ie CS01) must be computed 
MAR20.5
with respect to the names underlying the securitisation or nth-to-default 
instrument.
(2)
Delta CSR securitisation (CTP): the CSR correlation trading delta risk factors 
are defined along two dimensions:
(a)
the relevant underlying credit spread curves (bond and CDS); and
(b)
the following tenors: 0.5 years, 1 year, 3 years, 5 years and 10 years, to 
which delta risk factors are assigned.
(3)
Vega CSR securitisation (CTP): the vega risk factors are the implied volatilities 
of options that reference CTP credit spreads as underlyings (bond and CDS), 
as defined along one dimension, the maturity of the option. This is defined 
as the implied volatility of the option as mapped to one or several of the 
following maturity tenors: 0.5 years, 1 year, 3 years, 5 years and 10 years.
(4)
Curvature CSR securitisation (CTP): the CSR correlation trading curvature risk 
factors are defined along one dimension, the relevant underlying credit 
spread curves (bond and CDS). For instance, the bond-inferred spread curve 
of a given name within an iTraxx series and the CDS-inferred spread curve of
that given underlying would be considered a single spread curve. For the 
calculation of sensitivities, all the tenors are to be shifted in parallel.
FAQ
The second FAQ under 
 is also relevant to this paragraph.
MAR21.8
FAQ1
May risk weights be floored for credit spreads when applying the risk 
weights for the CSR risk classes?
No such floor is permitted in the market risk standard for the CSR risk 
classes, except for CSR curvature under the conditions set out in the 
second FAQ under 
.
MAR21.99
FAQ2
Equity risk factors
21.12
(1)
Delta equity: the equity delta risk factors are:
(a)
all the equity spot prices; and
(b)
all the equity repurchase agreement rates (equity repo rates).
(2)
Vega equity:
(a)
The equity vega risk factors are the implied volatilities of options that 
reference the equity spot prices as underlyings as defined along one 
dimension, the maturity of the option. This is defined as the implied 
volatility of the option as mapped to one or several of the following 
maturity tenors: 0.5 years, 1 year, 3 years, 5 years and 10 years.
(b)
There is no vega risk capital requirement for equity repo rates.
(3)
Curvature equity:
(a)
The equity curvature risk factors are all the equity spot prices.
(b)
There is no curvature risk capital requirement for equity repo rates.
FAQ
The second FAQ under 
 is also relevant to this paragraph.
MAR21.8
FAQ1
The sensitivities-based approach defines the repo risk factor only in the 
context of equities and not for fixed income funding instruments (to the 
extent that these instruments fall within the trading book definition as 
trading-related repo-style transactions). Is it the intention that fixed 
income funding instruments be excluded from the equity repo 
treatment? If so, should such funding instruments be subject to the 
GIRR capital requirement – for example, by considering the repo curve 
for a given currency as a yield curve subject to interest rate shocks?
Repo rate risk factors for fixed income funding instruments are subject 
to the GIRR capital requirement. A relevant repo curve should be 
considered by currency.
FAQ2
Commodity risk factors 
21.13
(1)
Delta commodity: the commodity delta risk factors are all the commodity 
spot prices. However for some commodities such as electricity (which is 
defined to fall within bucket 3 (energy – electricity and carbon trading) in
the relevant risk factor can either be the spot or the forward price, 
MAR21.82
as transactions relating to commodities such as electricity are more frequent 
on the forward price than transactions on the spot price. Commodity delta 
risk factors are defined along two dimensions:
(a)
legal terms with respect to the delivery location6 of the commodity; and
(b)
time to maturity of the traded instrument at the following tenors: 0 
years, 0.25 years, 0.5 years, 1 year, 2 years, 3 years, 5 years, 10 years, 15 
years, 20 years and 30 years.
(2)
Vega commodity: the commodity vega risk factors are the implied volatilities 
of options that reference commodity spot prices as underlyings. No 
differentiation between commodity spot prices by the maturity of the 
underlying or delivery location is required. The commodity vega risk factors 
are further defined along one dimension, the maturity of the option. This is 
defined as the implied volatility of the option as mapped to one or several of 
the following maturity tenors: 0.5 years, 1 year, 3 years, 5 years and 10 years.
Footnotes
(3)
Curvature commodity: the commodity curvature risk factors are defined 
along only one dimension, the constructed curve (ie no term structure 
decomposition) per commodity spot prices. For the calculation of 
sensitivities, all tenors (as defined for delta commodity) are to be shifted in 
parallel.
For example, a contract that can be delivered in five ports can be 
considered having the same delivery location as another contract if 
and only if it can be delivered in the same five ports. However, it 
cannot be considered having the same delivery location as another 
contract that can be delivered in only four (or less) of those five ports.
6
FAQ
The second FAQ under 
 is also relevant to this paragraph.
MAR21.8
FAQ1
How are commodity delta risk factors computed for futures and 
forward contracts?
The current prices for futures and forward contracts should be used to 
compute the commodity delta risk factors. Commodity delta should be 
allocated to the relevant tenor based on the tenor of the futures and 
forward contract and given that spot commodity price positions should 
be slotted into the first tenor (0 years).
FAQ2
FX risk factors
21.14
(1)
Delta FX: the FX delta risk factors are defined below.
(a)
The FX delta risk factors are all the exchange rates between the currency 
in which an instrument is denominated and the reporting currency. For 
transactions that reference an exchange rate between a pair of non-
reporting currencies, the FX delta risk factors are all the exchange rates 
between:
(i)
the reporting currency; and
(ii)
both the currency in which an instrument is denominated and any 
other currencies referenced by the instrument.7
(b)
Subject to supervisory approval, FX risk may alternatively be calculated 
relative to a base currency instead of the reporting currency. In such 
case the bank must account for not only:
(i)
the FX risk against the base currency; but also
(ii)
the FX risk between the reporting currency and the base currency 
(ie translation risk).
(c)
The resulting FX risk calculated relative to the base currency as set out 
in (b) is converted to the capital requirements in the reporting currency 
using the spot reporting/base exchange rate reflecting the FX risk 
between the base currency and the reporting currency.
(d)
The FX base currency approach may be allowed under the following 
conditions:
(i)
To use this alternative, a bank may only consider a single currency 
as its base currency; and
(ii)
The bank shall demonstrate to the relevant supervisor that 
calculating FX risk relative to their proposed base currency provides 
an appropriate risk representation for their portfolio (for example, 
by demonstrating that it does not inappropriately reduce capital 
requirements relative to those that would be calculated without the 
base currency approach) and that the translation risk between the 
base currency and the reporting currency is taken into account.
(2)
Vega FX: the FX vega risk factors are the implied volatilities of options that 
reference exchange rates between currency pairs; as defined along one 
dimension, the maturity of the option. This is defined as the implied volatility 
of the option as mapped to one or several of the following maturity tenors: 
0.5 years, 1 year, 3 years, 5 years and 10 years.
Footnotes
(3)
Curvature FX: the FX curvature risk factors are defined below.
(a)
The FX curvature risk factors are all the exchange rates between the 
currency in which an instrument is denominated and the reporting 
currency. For transactions that reference an exchange rate between a 
pair of non-reporting currencies, the FX risk factors are all the exchange 
rates between:
(i)
the reporting currency; and
(ii)
both the currency in which an instrument is denominated and any 
other currencies referenced by the instrument.
(b)
Where supervisory approval for the base currency approach has been 
granted for delta risks, FX curvature risks shall also be calculated relative 
to a base currency instead of the reporting currency, and then 
converted to the capital requirements in the reporting currency using 
the spot reporting/base exchange rate.
(4)
No distinction is required between onshore and offshore variants of a 
currency for all FX delta, vega and curvature risk factors.
For example, for an FX forward referencing USD/JPY, the relevant risk 
factors for a CAD-reporting bank to consider are the exchange rates 
USD/CAD and JPY/CAD. If that CAD-reporting bank calculates FX risk 
relative to a USD base currency, it would consider separate deltas for 
the exchange rate JPY/USD risk and CAD/USD FX translation risk and 
then translate the resulting capital requirement to CAD at the USD
/CAD spot exchange rate.
7
FAQ
The second FAQ under 
 is also relevant to this paragraph.
MAR21.8
FAQ1
(4) states: “No distinction is required between onshore and 
MAR21.14
offshore variants of a currency for all FX delta, vega and curvature risk 
factors.” Does this also apply for deliverable/non-deliverable variants 
(eg KRO vs KRW, BRO vs BRL, INO vs INR)?
Yes. No distinction is required between deliverable and non-deliverable 
variants of a currency.
FAQ2
Sensitivities-based method: definition of sensitivities
Requirements on instrument price or pricing models for sensitivity calculation
Sensitivities for each risk class must be expressed in the reporting currency of the 
bank. 
21.15
For each risk factor defined in 
 to 
, sensitivities are calculated 
MAR21.8
MAR21.14
as the change in the market value of the instrument as a result of applying a 
specified shift to each risk factor, assuming all the other relevant risk factors are 
held at the current level as defined in 
 to 
. 
MAR21.17
MAR21.38

### MAR21.16 .94 address the calculation of counterparty credit risk for SFTs
21.16

FAQ
In the context of delta sensitivity calculations, is it acceptable to use 
alternative formulations of sensitivities calculations that yield results 
very close to the prescribed formulation of sensitivities calculations?
Yes, as per 
, a bank may make use of alternative 
MAR21.17
formulations of sensitivities based on pricing models that the bank’s 
independent risk control unit uses to report market risks or actual 
profits and losses to senior management. In doing so, the bank is to 
demonstrate to its supervisor that the alternative formulations of 
sensitivities yield results very close to the prescribed formulations.
FAQ1
In calculating the risk capital requirement under the sensitivities-based method in
, the bank must determine each delta and vega sensitivity and curvature 
MAR21
scenario based on instrument prices or pricing models that an independent risk 
control unit within a bank uses to report market risks or actual profits and losses 
to senior management.

### MAR21.17 .94 address the calculation of counterparty credit risk for SFTs
21.17

Sensitivity definitions for delta risk
FAQ
In the context of delta sensitivity calculations, is it acceptable to use 
alternative formulations of sensitivities calculations that yield results 
very close to the prescribed formulation of sensitivities calculations?
Yes, as per 
, a bank may make use of alternative 
MAR21.17
formulations of sensitivities based on pricing models that the bank’s 
independent risk control unit uses to report market risks or actual 
profits and losses to senior management. In doing so, the bank is to 
demonstrate to its supervisor that the alternative formulations of 
sensitivities yield results very close to the prescribed formulations.
FAQ1
Are banks permitted to choose between zero rate and market rate 
sensitivities for GIRR delta and curvature capital requirements?
states that banks must determine each delta sensitivity, 
MAR21.17
vega sensitivity and curvature scenario based on instrument prices or 
pricing models that an independent risk control unit within a bank uses 
to report market risks or actual profits and losses to senior 
management. Banks should use zero rate or market rate sensitivities 
consistent with the pricing models referenced in that paragraph.
FAQ2
A key assumption of the standardised approach for market risk is that a bank’s 
pricing models used in actual profit and loss reporting provide an appropriate 
basis for the determination of regulatory capital requirements for all market risks. 
To ensure such adequacy, banks must at a minimum establish a framework for 
prudent valuation practices that include the requirements of 
.
CAP50

### MAR21.18 .94 address the calculation of counterparty credit risk for SFTs
21.18

Delta GIRR: the sensitivity is defined as the PV01. PV01 is measured by changing 
the interest rate r at tenor t (r ) of the risk-free yield curve in a given currency by 1 
t
basis point (ie 0.0001 in absolute terms) and dividing the resulting change in the 
market value of the instrument (V ) by 0.0001 (ie 0.01%) as follows, where:
i

### MAR21.19 .94 address the calculation of counterparty credit risk for SFTs
21.19

(1)
r is the risk-free yield curve at tenor t; 
t
(2)
cs is the credit spread curve at tenor t; and
t
(3)
V is the market value of the instrument i as a function of the risk-free 
i
interest rate curve and credit spread curve:
FAQ
Are banks permitted to choose between zero rate and market rate 
sensitivities for GIRR delta and curvature capital requirements?
states that banks must determine each delta sensitivity, 
MAR21.17
vega sensitivity and curvature scenario based on instrument prices or 
pricing models that an independent risk control unit within a bank uses 
to report market risks or actual profits and losses to senior 
management. Banks should use zero rate or market rate sensitivities 
consistent with the pricing models referenced in that paragraph.
FAQ1
Delta CSR non-securitisation, securitisation (non-CTP) and securitisation (CTP): 
the sensitivity is defined as CS01. The CS01 (sensitivity) of an instrument i is 
measured by changing a credit spread cs at tenor t (cs ) by 1 basis point (ie 
t
0.0001 in absolute terms) and dividing the resulting change in the market value 
of the instrument (V ) by 0.0001 (ie 0.01%) as follows: 
i

### MAR21.20 .94 address the calculation of counterparty credit risk for SFTs
21.20

FAQ
In cases where the bank does not have counterparty-specific money 
market curves, can the bank proxy PV01 to CS01?
Yes. Proxying PV01 to CS01 is permitted for such money market 
instruments.
FAQ1
Delta equity spot: the sensitivity is measured by changing the equity spot price by 
1 percentage point (ie 0.01 in relative terms) and dividing the resulting change in 
the market value of the instrument (V ) by 0.01 (ie 1%) as follows, where:
i

### MAR21.21 .94 address the calculation of counterparty credit risk for SFTs
21.21

(1)
k is a given equity;
(2)
EQ is the market value of equity k; and 
k
(3)
V is the market value of instrument i as a function of the price of equity k.
i
Delta equity repo rates: the sensitivity is measured by applying a parallel shift to 
the equity repo rate term structure by 1 basis point (ie 0.0001 in absolute terms) 
and dividing the resulting change in the market value of the instrument V by 
i
0.0001 (ie 0.01%) as follows, where:

### MAR21.22 .94 address the calculation of counterparty credit risk for SFTs
21.22

(1)
k is a given equity;
(2)
 is the repo term structure of equity k; and
(3)
V is the market value of instrument i as a function of the repo term structure 
i
of equity k.
Delta commodity: the sensitivity is measured by changing the commodity spot 
price by 1 percentage point (ie 0.01 in relative terms) and dividing the resulting 
change in the market value of the instrument V by 0.01 (ie 1%) as follows, where:
i

### MAR21.23 .94 address the calculation of counterparty credit risk for SFTs
21.23

(1)
k is a given commodity;
(2)
CTY is the market value of commodity k; and
k
(3)
V is the market value of instrument i as a function of the spot price of 
i
commodity k:
Sensitivity definitions for vega risk
FAQ
In relation to the curvature risk capital requirement for the commodity 
risk class, 
 requires that the curvature risk weight is the 
MAR21.99
parallel shift of all the tenors for each curve based on the highest 
prescribed delta risk weight for each bucket. A parallel shift in MAR21.
implies that an additive shock (in absolute terms) is applied along 
99
the curve. However, 
 states that the shock applied to delta 
MAR21.23
commodity is a relative shock. How should the shock be applied to 
commodity curvature?
The sizes of upward and downward shocks applied to assess the net 
curvature risk capital requirement for a specific commodity´s curvature 
risk factor should be based on the risk weight connected to the 
curvature bucket where that commodity is classified, in accordance 
with 
 and 
. The same relative shocks should be 
MAR21.97
MAR21.82
applied to all curvature risk factors classified under the same bucket, 
defined along the dimension of the constructed curve (ie no term 
structure decomposition) per each commodity spot price, as described 
in 
(3). For example, the constructed curve for gold (with a 
MAR21.13
risk weight of 20%) would be shifted up by multiplying each tenor price 
by 1.2 and down by multiplying each tenor price by 0.8.
FAQ1
Delta FX: the sensitivity is measured by changing the exchange rate by 1 
percentage point (ie 0.01 in relative terms) and dividing the resulting change in 
the market value of the instrument V by 0.01 (ie 1%), where:
i

### MAR21.24 .94 address the calculation of counterparty credit risk for SFTs
21.24

(1)
k is a given currency;
(2)
FX is the exchange rate between a given currency and a bank’s reporting 
k
currency or base currency, where the FX spot rate is the current market price 
of one unit of another currency expressed in the units of the bank’s 
reporting currency or base currency; and
(3)
V is the market value of instrument i as a function of the exchange rate k:
i
The option-level vega risk sensitivity to a given risk factor8 is measured by 
multiplying vega by the implied volatility of the option as follows, where:
21.25
Footnotes
(1)
vega,
 , is defined as the change in the market value of the option
 as a
result of a small amount of change to the implied volatility
 ; and
(2)
the instrument’s vega and implied volatility used in the calculation of vega 
sensitivities must be sourced from pricing models used by the independent 
risk control unit of the bank.
As specified in the vega risk factor definitions in 
 to 
, 
MAR21.8
MAR21.14
the implied volatility of the option must be mapped to one or more 
maturity tenors.
8
The following sets out how to derive vega risk sensitivities in specific cases:
21.26
(1)
Options that do not have a maturity, are assigned to the longest prescribed 
maturity tenor, and these options are also assigned to the RRAO.
(2)
Options that do not have a strike or barrier and options that have multiple 
strikes or barriers, are mapped to strikes and maturity used internally to price 
the option, and these options are also assigned to the RRAO.
(3)
CTP securitisation tranches that do not have an implied volatility, are not 
subject to vega risk capital requirement. Such instruments may not, however, 
be exempt from delta and curvature risk capital requirements.
Requirements on sensitivity computations
FAQ
Under the sensitivities-based method, would a bank need to compute 
vega risk over the longest maturity for a cancellable swap? Would a 
bank also be required to compute residual risk for cancellable swaps?
In the case where options do not have a specified maturity (eg 
cancellable swaps), the bank must assign those options to the longest 
prescribed maturity tenor for vega risk sensitivities and also assign 
such options to the RRAO.
In the case of the bank viewing the optionality of the cancellable swap 
as a swaption, the bank must assign the swaption to the longest 
prescribed maturity tenor for vega risk sensitivities (as it does not have 
a specified maturity) and derive the residual maturity of the underlying 
of the option accordingly.
FAQ1
When computing a first-order sensitivity for instruments subject to optionality, 
banks should assume that the implied volatility either: 
21.27
(1)
remains constant, consistent with a “sticky strike” approach; or
(2)
follows a “sticky delta” approach, such that implied volatility does not vary 
with respect to a given level of delta.
For the calculation of vega sensitivities, the distribution assumptions (ie log-
normal assumptions or normal assumptions) for pricing models are applied as 
follows:

### MAR21.28 .94 address the calculation of counterparty credit risk for SFTs
21.28

(1)
For the computation of a vega GIRR or CSR sensitivity, banks may use either 
the log-normal or normal assumptions.
(2)
For the computation of a vega equity, commodity or FX sensitivity, banks 
must use the log-normal assumption.9
Footnotes
Treatment of index instruments and multi-underlying options
Since vega (
of an instrument is multiplied by its implied
volatility (
), the vega risk sensitivity for that instrument will be the
same under the log-normal assumption and the normal assumption. 
As a consequence, banks may use a log-normal or normal assumption 
for GIRR and CSR (in recognition of the trade-offs between constrained 
specification and computational burden for a standardised approach). 
For the other risk classes, banks must only use a log-normal 
assumption (in recognition that this is aligned with common practices 
across jurisdictions).
9
FAQ
If banks may use either a log-normal or normal assumption for vega 
GIRR, does this mean that the same log-normal or normal assumption 
should be applied to all currencies, or can the application be different 
for different currencies? For example, is a bank permitted to adopt a 
normal assumption for EUR and a log-normal assumption for USD?
To compute vega GIRR, banks may choose a mix of log-normal and 
normal assumptions for different currencies.
FAQ1
If, for internal risk management, a bank computes vega sensitivities using 
different definitions than the definitions set out in this standard, the bank may 
transform the sensitivities computed for internal risk management purposes to 
deduce the sensitivities to be used for the calculation of the vega risk measure.

### MAR21.29 .94 address the calculation of counterparty credit risk for SFTs
21.29

All vega sensitivities must be computed ignoring the impact of credit valuation 
adjustments (CVA). 
21.30
In the delta and curvature risk context: for index instruments and multi-
underlying options, a look-through approach should be used. However, a bank 
may opt not to apply the look-through approach for instruments referencing any 
listed and widely recognised and accepted equity or credit index, where:

### MAR21.31 .94 address the calculation of counterparty credit risk for SFTs
21.31

(1)
it is possible to look-through the index (ie the constituents and their 
respective weightings are known);
(2)
the index contains at least 20 constituents;
(3)
no single constituent contained within the index represents more than 25% 
of the total index;
(4)
the largest 10% of constituents represents less than 60% of the total index; 
and
(5)
the total market capitalisation of all the constituents of the index is no less 
than USD 40 billion.
FAQ
When certain conditions set out in 
 are satisfied for 
MAR21.31
instruments referencing any listed and widely recognised equity or 
credit index, a bank may opt not to apply the look-through approach. 
It is common for funds with diversified constituents to satisfy the 
conditions set out in 
. Are positions in funds and instruments 
MAR21.31
that reference them permitted to apply the no look-through approach 
using index buckets?
No. Capital requirements for equity investments in funds generally 
must be calculated in accordance with one of the three ways set out in
– the no look-through approach for equity and credit indices 
MAR21.36
cannot be applied to funds that do not track a listed and widely 
recognised index even if their holdings meet the criteria set out in
(1) to (5).
MAR21.31
Subject to the criteria in 
, however, equity investment funds 
MAR21.35
that invest purely in either equity or debt instruments to replicate a 
listed and widely-recognised index may be treated as if they were 
investments in the those equity or credit indices and apply the no look-
through approach available for credit and equity indices on those 
funds if those investments in funds meet the requirements set out in
to 
.
MAR21.31
MAR21.34
FAQ1
For a given instrument, irrespective of whether a look-through approach is 
adopted or not, the sensitivity inputs used for the delta and curvature risk 
calculation must be consistent.

### MAR21.32 .94 address the calculation of counterparty credit risk for SFTs
21.32

Where a bank opts not to apply the look-through approach in accordance with
, a single sensitivity shall be calculated to each widely recognised and 
MAR21.31
accepted index that an instrument references. The sensitivity to the index should 
be assigned to the relevant delta risk bucket defined in 
 and 
 
MAR21.53
MAR21.72
as follows:

### MAR21.33 .94 address the calculation of counterparty credit risk for SFTs
21.33

(1)
Where more than 75% of constituents in that index (taking into account the 
weightings of that index) would be mapped to a specific sector bucket (ie 
bucket 1 to bucket 11 for equity risk, or bucket 1 to bucket 16 for CSR), the 
sensitivity to the index shall be mapped to that single specific sector bucket 
and treated like any other single-name sensitivity in that bucket.
(2)
In all other cases, the sensitivity may be mapped to an "index" bucket (ie 
bucket 12 or bucket 13 for equity risk; or bucket 17 or bucket 18 for 
CSR). The same principle as above (1) applies when allocating sensitivities to 
a specific index bucket.
(a)
For equity risk, an equity index should be mapped to the large market 
cap and advanced economy indices bucket (ie bucket 12) if at least 75% 
of the constituents in that index (taking into account the weightings of 
that index) are both large cap and advanced economy equities. 
Otherwise, it should be mapped to the other equity indices bucket (ie 
bucket 13).
(b)
For CSR, a credit index should be mapped to the investment grade 
indices bucket (ie bucket 17) if at least 75% of the constituents in that 
index (taking into account the weightings of that index) are investment 
grade. Otherwise, it should be mapped to the high yield indices bucket 
(ie bucket 18).
A look-through approach must always be used for indices that do not meet the 
criteria set out in 
(2) to 
(5), and for any multi-underlying 
MAR21.31
MAR21.31
instruments that reference a bespoke set of equities or credit positions.

### MAR21.34 .94 address the calculation of counterparty credit risk for SFTs
21.34

(1)
Where a look-through approach is adopted, for index instruments and multi-
underlying options other than the CTP, the sensitivities to constituent risk 
factors from those instruments or options are allowed to net with 
sensitivities to single-name instruments without restriction.
(2)
Index CTP instruments cannot be broken down into its constituents (ie the 
index CTP should be considered a risk factor as a whole) and the above-
mentioned netting at the issuer level does not apply either.
(3)
Where a look-through approach is adopted, it shall be applied consistently 
through time10, and shall be used for all identical instruments that reference 
the same index.
Footnotes
Treatment of equity investments in funds
In other words, a bank can initially not apply a look-through approach, 
and later decide to apply it. However once applied (for a certain type of 
instrument referencing a particular index), the bank will require 
supervisory approval to revert to a “no look-through” approach.
10
FAQ
In accordance with 
(1), sensitivities to credit spread risk (CSR) 
MAR21.58
arising from the correlation trading portfolio (CTP) should be classified 
according to the same bucket structure as the one for CSR non-
securitisation, as set out in 
, except for index buckets (bucket 
MAR21.51
17 and bucket 18). Since an index CTP should be considered a risk 
factor as a whole and cannot be broken down into its constituents, as 
stated in 
(2), how should a bank determine which bucket to 
MAR21.34
assign the delta sensitivity of an index CTP instrument, given the 
aforementioned bucket structure?
The delta CSR sensitivity of an index CTP instrument should be 
assigned to a single specific delta sector bucket consistent with the 
characteristics of, at least, 75% of the index constituents (taking into 
account the weightings of that index), in accordance with 
(1). 
MAR21.33
If this is not possible, then the index should be assigned to bucket 16, 
“Other sector”. The sensitivity to that index CTP instrument should be 
considered and treated like any other single-name sensitivity assigned 
to that same sector bucket.
FAQ1
For equity investments in funds that can be looked through as set out in RBC25.8
(5)(a), banks must apply a look-through approach and treat the underlying 
positions of the fund as if the positions were held directly by the bank (taking 
into account the bank’s share of the equity of the fund, and any leverage in the 
fund structure), except for the funds that meet the following conditions:

### MAR21.35 .94 address the calculation of counterparty credit risk for SFTs
21.35

(1)
For funds that hold an index instrument that meets the criteria set out under
, banks must still apply a look-through and treat the underlying 
MAR21.31
positions of the fund as if the positions were held directly by the bank, but 
the bank may then choose to apply the “no look-through” approach for the 
index holdings of the fund as set out in 
. 
MAR21.33
(2)
For funds that track an index benchmark, a bank may opt not to apply the 
look-through approach and opt to measure the risk assuming the fund is a 
position in the tracked index only where:
(a)
the fund has an absolute value of a tracking difference (ignoring fees 
and commissions) of less than 1%; and
(b)
the tracking difference is checked at least annually and is defined as the 
annualised return difference between the fund and its tracked 
benchmark over the last 12 months of available data (or a shorter 
period in the absence of a full 12 months of data).
For equity investments in funds that cannot be looked through (ie do not meet 
the criterion set out in 
(5)(a)), but that the bank has access to daily price 
RBC25.8
quotes and knowledge of the mandate of the fund (ie meet both the criteria set 
out in 
(5)(b)), banks may calculate capital requirements for the fund in 
RBC25.8
one of three ways:

### MAR21.36 .94 address the calculation of counterparty credit risk for SFTs
21.36

(1)
If the fund tracks an index benchmark and meets the requirement set out in
(2)(a) and (b), the bank may assume that the fund is a position in 
MAR21.35
the tracked index, and may assign the sensitivity to the fund to relevant 
sector specific buckets or index buckets as set out in 
.
MAR21.33
(2)
Subject to supervisory approval, the bank may consider the fund as a 
hypothetical portfolio in which the fund invests to the maximum extent 
allowed under the fund’s mandate in those assets attracting the highest 
capital requirements under the sensitivities-based method, and then 
progressively in those other assets implying lower capital requirements. If 
more than one risk weight can be applied to a given exposure under the 
sensitivities-based method, the maximum risk weight applicable must be 
used.
(a)
This hypothetical portfolio must be subject to market risk capital 
requirements on a stand-alone basis for all positions in that fund, 
separate from any other positions subject to market risk capital 
requirements.
(b)
The counterparty credit and CVA risks of the derivatives of this 
hypothetical portfolio must be calculated using the simplified 
methodology set out in accordance with 
(c) of the banking 
CRE60.7
book equity investment in funds treatment.
Treatment of vega risk for multi-underlying instruments
Footnotes
(3)
A bank may treat their equity investment in the fund as an unrated equity 
exposure to be allocated to the “other sector” bucket (bucket 11). In applying 
this treatment, banks must also consider whether, given the mandate of the 
fund, the default risk capital (DRC) requirement risk weight prescribed to the 
fund is sufficiently prudent (as set out in 
), and whether the RRAO 
MAR22.8
should apply (as set out in 
). 
MAR23.6
As per the requirement in 
(5), net long equity investments in a given fund 
RBC25.8
in which the bank cannot look through or does not meet the requirements of
(5) for the fund must be assigned to the banking book. Net short 
RBC25.8
positions in funds, where the bank cannot look through or does not meet the 
requirements of 
(5), must be excluded from any trading book capital 
RBC25.8
requirements under the market risk framework, with the net position instead 
subjected to a 100% capital requirement.

### MAR21.37 .94 address the calculation of counterparty credit risk for SFTs
21.37

In the vega risk context: 
21.38
(1)
Multi-underlying options (including index options) are usually priced based 
on the implied volatility of the option, rather than the implied volatility of its 
underlying constituents and a look-through approach may not need to be 
applied, regardless of the approach applied to the delta and curvature risk 
calculation as set out in 
 through 
.
MAR21.31
MAR21.34 11
(2)
For indices, the vega risk with respect to the implied volatility of the multi-
underlying options will be calculated using a sector specific bucket or an 
index bucket defined in 
 and 
 as follows:
MAR21.53
MAR21.72
(a)
Where more than 75% of constituents in that index (taking into account 
the weightings of that index) would be mapped to a single specific 
sector bucket (ie bucket 1 to bucket 11 for equity risk; or bucket 1 to 
bucket 16 for CSR), the sensitivity to the index shall be mapped to that 
single specific sector bucket and treated like any other single-name 
sensitivity in that bucket.
(b)
In all other cases, the sensitivity may be mapped to an “index” bucket (ie 
bucket 12 or bucket 13 for equity risk or bucket 17 or bucket 18 for CSR).
As specified in the vega risk factor definitions in 
 to 
, 
MAR21.8
MAR21.14
the implied volatility of an option must be mapped to one or more 
maturity tenors.
11
Sensitivities-based method: definition of delta risk buckets, risk 
weights and correlations
Delta GIRR buckets, risk weights and correlations
Footnotes
to 
 set out buckets, risk weights and correlation parameters 
MAR21.41
MAR21.89
for each risk class to calculate delta risk capital requirement as set out in 
.
MAR21.4
21.39
The prescribed risk weights and correlations in 
 to 
 have 
MAR21.41
MAR21.89
been calibrated to the liquidity adjusted time horizon related to each risk class.
21.40
Each currency is a separate delta GIRR bucket, so all risk factors in risk-free yield 
curves for the same currency in which interest rate-sensitive instruments are 
denominated are grouped into the same bucket.

### MAR21.41 .94 address the calculation of counterparty credit risk for SFTs
21.41

For calculating weighted sensitivities, the risk weights for each tenor in risk-free 
yield curves are set in Table 1 as follows:
21.42
Delta GIRR buckets and risk weights
Table 1
Tenor
0.25 year
0.5 year
1 year
2 year
3 year
Risk weight
1.7%
1.7%
1.6%
1.3%
1.2%
Tenor
5 year
10 year
15 year
20 year
30 year
Risk weight (percentage 
points)
1.1%
1.1%
1.1%
1.1%
1.1%
The risk weight for the inflation risk factor and the cross-currency basis risk 
factors, respectively, is set at 1.6%. 
21.43
For specified currencies by the Basel Committee,12 the above risk weights may, at 
the discretion of the bank, be divided by the square root of 2.
21.44
Specified currencies by the Basel Committee are: EUR, USD, GBP, AUD, 
JPY, SEK, CAD as well as the domestic reporting currency of a bank.
12
For aggregating GIRR risk positions within a bucket, the correlation parameter
between weighted sensitivities
 and
 within the same bucket (ie same
currency), same assigned tenor, but different curves is set at 99.90%. In 
aggregating delta risk positions for cross-currency basis risk for onshore and 
offshore curves, which must be considered two different curves as set out in
, a bank may choose to aggregate all cross-currency basis risk for a 
MAR21.8
currency (ie “Curr/USD” or “Curr/EUR”) for both onshore and offshore curves by a 
simple sum of weighted sensitivities.

### MAR21.45 .94 address the calculation of counterparty credit risk for SFTs
21.45

The delta risk correlation
 between weighted sensitivities
 and
 within
the same bucket with different tenor and same curve is set in the following Table 
213:

### MAR21.46 .94 address the calculation of counterparty credit risk for SFTs
21.46

Delta GIRR correlations (
 ) within the same bucket, with different tenor and same
curve
T
0.25 
year
0.5 
year
1 year
2 year
3 year
5 year
10 
year
15 
year
20 
year
0.25 
year
100.0%
97.0%
91.4%
81.1%
71.9%
56.6%
40.0%
40.0%
40.0%
0.5 
year
97.0%
100.0%
97.0%
91.4%
86.1%
76.3%
56.6%
41.9%
40.0%
1 
year
91.4%
97.0%
100.0%
97.0%
94.2%
88.7%
76.3%
65.7%
56.6%
2 
year
81.1%
91.4%
97.0%
100.0%
98.5%
95.6%
88.7%
82.3%
76.3%
3 
year
71.9%
86.1%
94.2%
98.5%
100.0%
98.0%
93.2%
88.7%
84.4%
5 
year
56.6%
76.3%
88.7%
95.6%
98.0%
100.0%
97.0%
94.2%
91.4%
10 
year
40.0%
56.6%
76.3%
88.7%
93.2%
97.0%
100.0%
98.5%
97.0%
15 
year
40.0%
41.9%
65.7%
82.3%
88.7%
94.2%
98.5%
100.0%
99.0%
20 
year
40.0%
40.0%
56.6%
76.3%
84.4%
91.4%
97.0%
99.0%
100.0%
30 
year
40.0%
40.0%
41.9%
65.7%
76.3%
86.1%
94.2%
97.0%
98.5%
1
Footnotes
Footnotes
The delta GIRR correlation parameters (
) set out in Table 2 is
determined by
, where T (respectively T ) is 
 
 
k
l
the tenor that relates to
(respectively
); and
is set at
3%. For example, the correlation between a sensitivity to the one-year 
tenor of the Eonia swap curve and the a sensitivity to the five-year 
tenor of the Eonia swap curve in the same currency is
.
13
Between two weighted sensitivities
 and
 within the same bucket with
different tenor and different curves, the correlation
 is equal to the correlation
parameter specified in 
 multiplied by 99.90%.
MAR21.46
14

### MAR21.47 .94 address the calculation of counterparty credit risk for SFTs
21.47

For example, the correlation between a sensitivity to the one-year 
tenor of the Eonia swap curve and a sensitivity to the five-year tenor of 
the three-month Euribor swap curve in the same currency is
.
14
FAQ
What should the correlation between two inflation curves in the same 
currency (eg German vs French, in Euro) be for GIRR?
Per 
, a 99.90% correlation should apply to different inflation 
MAR21.47
curves in the same currency.
FAQ1
The delta risk correlation
 between a weighted sensitivity
 to the inflation
curve and a weighted sensitivity
 to a given tenor of the relevant yield curve is
40%.

### MAR21.48 .94 address the calculation of counterparty credit risk for SFTs
21.48

Delta CSR non-securitisations buckets, risk weights and correlations
The delta risk correlation
 between a weighted sensitivity
 to a cross-
currency basis curve and a weighted sensitivity
 to each of the following
curves is 0%:

### MAR21.49 .94 address the calculation of counterparty credit risk for SFTs
21.49

(1)
a given tenor of the relevant yield curve;
(2)
the inflation curve; or
(3)
another cross-currency basis curve (if relevant).
For aggregating GIRR risk positions across different buckets (ie different
currencies), the parameter
 is set at 50%.

### MAR21.50 .94 address the calculation of counterparty credit risk for SFTs
21.50

For delta CSR non-securitisations, buckets are set along two dimensions - credit 
quality and sector - as set out in Table 3. The CSR non-securitisation sensitivities 
or risk exposures should first be assigned to a bucket defined before calculating 
weighted sensitivities by applying a risk weight.

### MAR21.51 .94 address the calculation of counterparty credit risk for SFTs
21.51

Buckets for delta CSR non-securitisations
Table 3
Bucket 
number
Credit quality
Sector
1
Investment
grade (IG)
Sovereigns including central banks, multilateral 
development banks
2
Local government, government-backed non-financials, 
education, public administration
3
Financials including government-backed financials
4
Basic materials, energy, industrials, agriculture, 
manufacturing, mining and quarrying
5
Consumer goods and services, transportation and storage, 
administrative and support service activities
6
Technology, telecommunications
7
Health care, utilities, professional and technical activities
8
Covered bonds15
9
High yield 
(HY) & non-
rated (NR)
Sovereigns including central banks, multilateral 
development banks
10
Local government, government-backed non-financials, 
education, public administration
11
Financials including government-backed financials
12
Basic materials, energy, industrials, agriculture, 
manufacturing, mining and quarrying
13
Consumer goods and services, transportation and storage, 
administrative and support service activities
14
Technology, telecommunications
15
Health care, utilities, professional and technical activities
16
Other sector16
17
IG indices
18
HY indices
Footnotes
Covered bonds must meet the definition provided in 
, 
LEX30.37 LEX30.39
and 
.
LEX30.40
15
Credit quality is not a differentiating consideration for this bucket.
16
FAQ
How are risk weights to be determined when external ratings assigned 
by credit rating agencies differ and when there are no external ratings 
available?
Consistent with the treatment of external ratings under the 
standardised approach to credit risk (see 
 and 
), if 
CRE21.10
CRE21.11
there are two ratings which map into different risk weights, the higher 
risk weight should be applied. If there are three or more ratings with 
different risk weights, the ratings corresponding to the two lowest risk 
weights should be referred to and the higher of those two risk weights 
will be applied.
Consistent with the treatment where there are no external ratings 
under the CVA risk chapter (see 
), where there are no 
MAR50.16
external ratings or where external ratings are not recognised within a 
jurisdiction, banks may, subject to supervisory approval:
for the purpose of assigning delta CSR non-securitisation risk 
weights, map the internal rating to an external rating, and assign 
a risk weight corresponding to either “investment grade” or “high 
yield” in 
;
MAR21.51
for the purpose of assigning default risk weights under the DRC 
requirement, map the internal rating to an external rating, and 
assign a risk weight corresponding to one of the seven external 
ratings in the table included 
; or
MAR22.24
apply the risk weights specified in 
 and 
 for 
MAR21.51
MAR22.24
unrated/non-rated categories.
FAQ1
For the purpose of market risk capital requirements, what are the CSR 
capital requirements for Fannie Mae and Freddie Mac mortgage-
backed security (MBS) bonds? What is the loss-given-default (LGD) for 
Fannie and Freddie MBS?
FAQ2
Non-tranched MBS issued by government sponsored-entities (GSEs), 
such as Fannie and Freddie, are assigned to bucket 2 (local 
government, government-backed non-financials, education, public 
administration) for CSR with a risk weight of 1.0%.
In accordance with 
, the LGD for non-tranched MBS issued 
MAR22.12
by GSEs is 75% (ie the LGD assigned to senior debt instruments) unless 
the GSE security satisfies the requirements of footnote 15 to 
 
MAR21.51
for treatment of the security as a covered bond.
To assign a risk exposure to a sector, banks must rely on a classification that is 
commonly used in the market for grouping issuers by industry sector. 
21.52
(1)
The bank must assign each issuer to one and only one of the sector buckets 
in the table under 
. 
MAR21.51
(2)
Risk positions from any issuer that a bank cannot assign to a sector in this 
fashion must be assigned to the other sector (ie bucket 16).
For calculating weighted sensitivities, the risk weights for buckets 1 to 18 are set 
out in Table 4. Risk weights are the same for all tenors (ie 0.5 years, 1 year, 3 
years, 5 years, 10 years) within each bucket:

### MAR21.53 .94 address the calculation of counterparty credit risk for SFTs
21.53

Footnotes
Risk weights for buckets for delta CSR non-securitisations
Table 4
Bucket number
Risk weight
1
0.5%
2
1.0%
3
5.0%
4
3.0%
5
3.0%
6
2.0%
7
1.5%
8
2.5%17
9
2.0%
10
4.0%
11
12.0%
12
7.0%
13
8.5%
14
5.5%
15
5.0%
16
12.0%
17
1.5%
18
5.0%
For covered bonds that are rated AA- or higher, the applicable risk 
weight may at the discretion of the bank be 1.5%.
17
Footnotes
For buckets 1 to 15, for aggregating delta CSR non-securitisations risk positions
within a bucket, the correlation parameter
 between two weighted sensitivities
and
 within the same bucket, is set as follows, where:18

### MAR21.54 .94 address the calculation of counterparty credit risk for SFTs
21.54

(1)
 is equal to 1 where the two names of sensitivities k and l are identical,
and 35% otherwise;
(2)
 is equal to 1 if the two tenors of the sensitivities k and l are identical,
and to 65% otherwise; and
(3)
 is equal to 1 if the two sensitivities are related to same curves, and
99.90% otherwise.
For example, a sensitivity to the five-year Apple bond curve and a 
sensitivity to the 10-year Google CDS curve would be:
.
18
FAQ
(3) explicitly states that, for CSR curvature, the bond-CDS 
MAR21.9
basis is ignored. Is it correct that, under 
(1), bond and CDS 
MAR21.9
curves are considered distinct risk factors and the only “basis” taken
into account in
in 
 and 
 is the bond-CDS 
 
 
MAR21.54
MAR21.55
basis?
Yes. Bond and CDS credit spreads are considered distinct risk factors
under 
(1), and
referenced in 
 and 
 
MAR21.9
 
 
MAR21.54
MAR21.55
is meant to capture only the bond-CDS basis.
FAQ1
For buckets 17 and 18, for aggregating delta CSR non-securitisations risk
positions within a bucket, the correlation parameter
 between two weighted
sensitivities
 and
 within the same bucket is set as follows, where:

### MAR21.55 .94 address the calculation of counterparty credit risk for SFTs
21.55

(1)
 is equal to 1 where the two names of sensitivities k and l are identical,
and 80% otherwise;
(2)
 is equal to 1 if the two tenors of the sensitivities k and l are identical,
and to 65% otherwise; and
(3)
 is equal to 1 if the two sensitivities are related to same curves, and
99.90% otherwise.
The correlations above do not apply to the other sector bucket (ie bucket 16).
21.56
(1)
The aggregation of delta CSR non-securitisation risk positions within the 
other sector bucket would be equal to the simple sum of the absolute values 
of the net weighted sensitivities allocated to this bucket. The same method 
applies to the aggregation of vega risk positions.
(2)
The aggregation of curvature CSR non-securitisation risk positions within the 
other sector bucket would be calculated by the formula below.
For aggregating delta CSR non-securitisation risk positions across buckets 1 to
18, the correlation parameter
 is set as follows, where:

### MAR21.57 .94 address the calculation of counterparty credit risk for SFTs
21.57

(1)
 is equal to 50% where the two buckets b and c are both in buckets 1
to 15 and have a different rating category (either IG or HY/NR).
 is
equal to 1 otherwise; and
(2)
 is equal to 1 if the two buckets belong to the same sector, and to the
specified numbers in Table 5 otherwise.
Values of
 where the buckets do not belong to the same sector
Table 5
Bucket
1 
/ 9
2 / 
10
3 / 
11
4 / 
12
5 / 
13
6 / 
14
7 / 
15
8
16
17
18
1 / 9
 
75%
10%
20%
25%
20%
15%
10%
0%
45%
45%
2 / 10
 
 
5%
15%
20%
15%
10%
10%
0%
45%
45%
3 / 11
 
 
 
5%
15%
20%
5%
20%
0%
45%
45%
4 / 12
 
 
 
 
20%
25%
5%
5%
0%
45%
45%
5 / 13
 
 
 
 
 
25%
5%
15%
0%
45%
45%
6 / 14
 
 
 
 
 
 
5%
20%
0%
45%
45%
7 / 15
 
 
 
 
 
 
 
5%
0%
45%
45%
8
 
 
 
 
 
 
 
 
0%
45%
45%
16
 
 
 
 
 
 
 
 
 
0%
0%
17
 
 
 
 
 
 
 
 
 
 
75%
18
Delta CSR securitisation (CTP) buckets, risk weights and correlations
Sensitivities to CSR arising from the CTP and its hedges are treated as a separate 
risk class as set out in 
. The buckets, risk weights and correlations for the 
MAR21.1
CSR securitisations (CTP) apply as follows:

### MAR21.58 .94 address the calculation of counterparty credit risk for SFTs
21.58

(1)
The same bucket structure and correlation structure apply to the CSR 
securitisations (CTP) as those for the CSR non-securitisation framework as set 
out in 
 to 
 with an exception of index buckets (ie buckets 
MAR21.51
MAR21.57
17 and 18).
(2)
The risk weights and correlation parameters of the delta CSR non-
securitisations are modified to reflect longer liquidity horizons and larger 
basis risk as specified in 
 to 
.
MAR21.59
MAR21.61
FAQ
In accordance with 
(1), sensitivities to credit spread risk (CSR) 
MAR21.58
arising from the correlation trading portfolio (CTP) should be classified 
according to the same bucket structure as the one for CSR non-
securitisation, as set out in 
, except for index buckets (bucket 
MAR21.51
17 and bucket 18). Since an index CTP should be considered a risk 
factor as a whole and cannot be broken down into its constituents, as 
stated in 
(2), how should a bank determine which bucket to 
MAR21.34
assign the delta sensitivity of an index CTP instrument, given the 
aforementioned bucket structure?
The delta CSR sensitivity of an index CTP instrument should be 
assigned to a single specific delta sector bucket consistent with the 
characteristics of, at least, 75% of the index constituents (taking into 
account the weightings of that index), in accordance with 
(1). 
MAR21.33
If this is not possible, then the index should be assigned to bucket 16, 
“Other sector”. The sensitivity to that index CTP instrument should be 
considered and treated like any other single-name sensitivity assigned 
to that same sector bucket.
FAQ1
For calculating weighted sensitivities, the risk weights for buckets 1 to 16 are set 
out in Table 6. Risk weights are the same for all tenors (ie 0.5 years, 1 year, 3 
years, 5 years, 10 years) within each bucket:

### MAR21.59 .94 address the calculation of counterparty credit risk for SFTs
21.59

Risk weights for sensitivities to CSR arising from the CTP
Table 6
Bucket number
Risk weight
1
4.0%
2
4.0%
3
8.0%
4
5.0%
5
4.0%
6
3.0%
7
2.0%
8
6.0%
9
13.0%
10
13.0%
11
16.0%
12
10.0%
13
12.0%
14
12.0%
15
12.0%
16
13.0%
For aggregating delta CSR securitisations (CTP) risk positions within a bucket, the
delta risk correlation
 is derived the same way as in 
 and 
, 
MAR21.54
MAR21.55
except that the correlation parameter applying when the sensitivities are not
related to same curves,
 , is modified.

### MAR21.60 .94 address the calculation of counterparty credit risk for SFTs
21.60

Delta CSR securitisation (non-CTP) buckets, risk weights and correlations
(1)
 is now equal to 1 if the two sensitivities are related to same curves,
and 99.00% otherwise.
(2)
The identical correlation parameters for
 and
 to CSR non-
securitisation as set out in 
 and 
 apply.
MAR21.54
MAR21.55
For aggregating delta CSR securitisations (CTP) risk positions across buckets, the
correlation parameters for
 are identical to CSR non-securitisation as set out in
.
MAR21.57

### MAR21.61 .94 address the calculation of counterparty credit risk for SFTs
21.61

For delta CSR securitisations not in the CTP, buckets are set along two 
dimensions – credit quality and sector – as set out in Table 7. The delta CSR 
securitisation (non-CTP) sensitivities or risk exposures must first be assigned to a 
bucket before calculating weighted sensitivities by applying a risk weight.

### MAR21.62 .94 address the calculation of counterparty credit risk for SFTs
21.62

Buckets for delta CSR securitisations (non-CTP)
Table 7
Bucket number
Credit quality
Sector
1
Senior investment grade 
(IG)
RMBS – Prime
2
RMBS – Mid-prime
3
RMBS – Sub-prime
4
CMBS
5
Asset-backed securities (ABS) – Student 
loans
6
ABS – Credit cards
7
ABS – Auto
8
Collateralised loan obligation (CLO) non-
CTP
9
Non-senior IG
RMBS – Prime
10
RMBS – Mid-prime
11
RMBS – Sub-prime
12
Commercial mortgage-backed 
securities (CMBS)
13
ABS – Student loans
14
ABS – Credit cards
15
ABS – Auto
16
CLO non-CTP
17
High yield & non-rated
RMBS – Prime
18
RMBS – Mid-prime
19
RMBS – Sub-prime
20
CMBS
21
ABS – Student loans
Footnotes
22
ABS – Credit cards
23
ABS – Auto
24
CLO non-CTP
25
Other sector19
Credit quality is not a differentiating consideration for this bucket.
19
To assign a risk exposure to a sector, banks must rely on a classification that is 
commonly used in the market for grouping tranches by type. 
21.63
(1)
The bank must assign each tranche to one of the sector buckets in above 
Table 7.
(2)
Risk positions from any tranche that a bank cannot assign to a sector in this 
fashion must be assigned to the other sector (ie bucket 25).
For calculating weighted sensitivities, the risk weights for buckets 1 to 8 (senior 
IG) are set out in Table 8:
21.64
Risk weights for buckets 1 to 8 for delta CSR securitisations (non-CTP)
Table 8
Bucket number
Risk weight (in percentage points)
1
0.9%
2
1.5%
3
2.0%
4
2.0%
5
0.8%
6
1.2%
7
1.2%
8
1.4%
The risk weights for buckets 9 to 16 (non-senior investment grade) are then equal 
to the corresponding risk weights for buckets 1 to 8 scaled up by a multiplication
by 1.25. For instance, the risk weight for bucket 9 is equal to
 .

### MAR21.65 .94 address the calculation of counterparty credit risk for SFTs
21.65

The risk weights for buckets 17 to 24 (high yield and non-rated) are then equal to 
the corresponding risk weights for buckets 1 to 8 scaled up by a multiplication by
1.75. For instance, the risk weight for bucket 17 is equal to
 .

### MAR21.66 .94 address the calculation of counterparty credit risk for SFTs
21.66

The risk weight for bucket 25 is set at 3.5%.
21.67
For aggregating delta CSR securitisations (non-CTP) risk positions within a
bucket, the correlation parameter
 between two sensitivities
 and
within the same bucket, is set as follows, where:

### MAR21.68 .94 address the calculation of counterparty credit risk for SFTs
21.68

(1)
 is equal to 1 where the two names of sensitivities k and l are within
the same bucket and related to the same securitisation tranche (more than 
80% overlap in notional terms), and 40% otherwise;
(2)
 is equal to 1 if the two tenors of the sensitivities k and l are identical,
and to 80% otherwise; and
(3)
 is equal to 1 if the two sensitivities are related to same curves, and
99.90% otherwise.
FAQ
includes
, which equals 1 where the two 
MAR21.68
sensitivities within the same bucket are related to the same 
securitisation tranche, or 40% otherwise. There is no issuer factor. Does 
this mean that two sensitivities relating to the same issuer but different 
tranches require 40% correlation?
Yes. There is no granularity for issuers in the delta CSR securitisation 
part as set out in 
. Where two tranches have exactly the 
MAR21.10
same issuer, same tenor and same basis, but different tranches (ie 
different credit quality), the correlation must be 40%.
FAQ1
The correlations above do not apply to the other sector bucket (ie bucket 25).
21.69
(1)
The aggregation of delta CSR securitisations (non-CTP) risk positions within 
the other sector bucket would be equal to the simple sum of the absolute 
values of the net weighted sensitivities allocated to this bucket. The same 
method applies to the aggregation of vega risk positions.
(2)
The aggregation of curvature CSR risk positions within the other sector 
bucket would be calculated by the formula below.
For aggregating delta CSR securitisations (non-CTP) risk positions across buckets
1 to 24, the correlation parameter
 is set as 0%.

### MAR21.70 .94 address the calculation of counterparty credit risk for SFTs
21.70

Equity risk buckets, risk weights and correlations
For aggregating delta CSR securitisations (non-CTP) risk positions between the 
other sector bucket (ie bucket 25) and buckets 1 to 24, (i) the capital 
requirements for bucket 25 and (ii) the aggregated capital requirements for
buckets 1 to 24 will be simply summed up to the overall risk class level capital 
requirements. There should be no diversification or hedging effects recognised in 
aggregating the capital requirements for the other sector bucket (ie bucket 25) 
with those for buckets 1 to 24.

### MAR21.71 .94 address the calculation of counterparty credit risk for SFTs
21.71

For delta equity risk, buckets are set along three dimensions – market 
capitalisation, economy and sector – as set out in Table 9. The equity risk 
sensitivities or exposures must first be assigned to a bucket before calculating 
weighted sensitivities by applying a risk weight.

### MAR21.72 .94 address the calculation of counterparty credit risk for SFTs
21.72

Buckets for delta sensitivities to equity risk
Table 9
Bucket 
number
Market
cap
Economy
Sector
1
Large
Emerging
market 
economy
Consumer goods and services, 
transportation and storage, administrative
and support service activities, healthcare,
utilities
2
Telecommunications, industrials
3
Basic materials, energy, agriculture, 
manufacturing, mining and quarrying
4
Financials including government-backed 
financials, real estate activities, technology
5
Advanced
economy
Consumer goods and services, 
transportation and storage, administrative
and support service activities, healthcare,
utilities
6
Telecommunications, industrials
7
Basic materials, energy, agriculture, 
manufacturing, mining and quarrying
8
Financials including government-backed 
financials, real estate activities, technology
9
Small
Emerging
market 
economy
All sectors described under bucket
numbers 1, 2, 3 and 4
10
Advanced
economy
All sectors described under bucket
numbers 5, 6, 7 and 8
11
Other sector20
12
Large market cap, advanced economy equity indices (non-sector specific)
13
Other equity indices (non-sector specific)
Footnotes
Market capitalisation or economy (ie advanced or emerging market) is 
not a differentiating consideration for this bucket.
20
Market capitalisation (market cap) is defined as the sum of the market 
capitalisations based on the market value of the total outstanding shares issued 
by the same listed legal entity or a group of legal entities across all stock markets 
globally, where the total outstanding shares issued by the group of legal entities 
refer to cases where the listed entity is a parent company of a group of legal 
entities. Under no circumstances should the sum of the market capitalisations of 
multiple related listed entities be used to determine whether a listed entity is 
“large market cap” or “small market cap”.

### MAR21.73 .94 address the calculation of counterparty credit risk for SFTs
21.73

Large market cap is defined as a market capitalisation equal to or greater than 
USD 2 billion and small market cap is defined as a market capitalisation of less 
than USD 2 billion.

### MAR21.74 .94 address the calculation of counterparty credit risk for SFTs
21.74

The advanced economies are Canada, the United States, Mexico, the euro area, 
the non-euro area western European countries (the United Kingdom, Norway, 
Sweden, Denmark and Switzerland), Japan, Oceania (Australia and New Zealand), 
Singapore and Hong Kong SAR.

### MAR21.75 .94 address the calculation of counterparty credit risk for SFTs
21.75

FAQ
Are the countries referenced in 
 to be understood as country 
MAR21.75
of incorporation?
An equity issuer must be allocated to a particular bucket according to 
the most material country or region in which the issuer operates. As 
stated in 
: “For multinational multi-sector equity issuers, the 
MAR21.76
allocation to a particular bucket must be done according to the most 
material region and sector in which the issuer operates.
FAQ1
To assign a risk exposure to a sector, banks must rely on a classification that is 
commonly used in the market for grouping issuers by industry sector. 
21.76
(1)
The bank must assign each issuer to one of the sector buckets in the table 
under 
 and it must assign all issuers from the same industry to the 
MAR21.72
same sector.
(2)
Risk positions from any issuer that a bank cannot assign to a sector in this 
fashion must be assigned to the other sector (ie bucket 11).
(3)
For multinational multi-sector equity issuers, the allocation to a particular 
bucket must be done according to the most material region and sector in 
which the issuer operates.
For calculating weighted sensitivities, the risk weights for the sensitivities to each 
of equity spot price and equity repo rates for buckets 1 to 13 are set out in Table 
10:

### MAR21.77 .94 address the calculation of counterparty credit risk for SFTs
21.77

Risk weights for buckets 1 to 13 for sensitivities to equity risk
Table 10
Bucket number
Risk weight for equity spot
price
Risk weight for equity repo
rate
1
55%
0.55%
2
60%
0.60%
3
45%
0.45%
4
55% 
0.55%
5
30%
0.30%
6
35%
0.35%
7
40%
0.40%
8
50%
0.50%
9
70%
0.70%
10
50%
0.50%
11
70%
0.70%
12
15%
0.15%
13
25%
0.25%
For aggregating delta equity risk positions within a bucket, the correlation
parameter
 between two sensitivities
 and
 within the same bucket is
set at as follows

### MAR21.78 .94 address the calculation of counterparty credit risk for SFTs
21.78

(1)
The correlation parameter
 is set at 99.90%, where:
(a)
one is a sensitivity to an equity spot price and the other a sensitivity to 
an equity repo rates; and
(b)
both are related to the same equity issuer name.
(2)
The correlation parameter
 is set out in (a) to (e) below, where both
sensitivities are to equity spot price, and where:
(a)
15% between two sensitivities within the same bucket that fall under 
large market cap, emerging market economy (bucket number 1, 2, 3 or 
4).
(b)
25% between two sensitivities within the same bucket that fall under 
large market cap, advanced economy (bucket number 5, 6, 7 or 8).
(c)
7.5% between two sensitivities within the same bucket that fall under 
small market cap, emerging market economy (bucket number 9).
(d)
12.5% between two sensitivities within the same bucket that fall under 
small market cap, advanced economy (bucket number 10).
(e)
80% between two sensitivities within the same bucket that fall under 
either index bucket (bucket number 12 or 13).
(3)
The same correlation parameter
 as set out in above (2)(a) to (e) apply,
where both sensitivities are to equity repo rates.
(4)
The correlation parameter
 is set as each parameter specified in above (2)
(a) to (e) multiplied by 99.90%, where:
(a)
One is a sensitivity to an equity spot price and the other a sensitivity to 
an equity repo rate; and
(b)
Each sensitivity is related to a different equity issuer name.
The correlations set out above do not apply to the other sector bucket (ie bucket 
11). 
21.79
Commodity risk buckets, risk weights and correlations
(1)
The aggregation of equity risk positions within the other sector bucket 
capital requirement would be equal to the simple sum of the absolute values 
of the net weighted sensitivities allocated to this bucket. The same method 
applies to the aggregation of vega risk positions.
(2)
The aggregation of curvature equity risk positions within the other sector 
bucket (ie bucket 11) would be calculated by the formula:
For aggregating delta equity risk positions across buckets 1 to 13, the correlation
parameter
 is set at:

### MAR21.80 .94 address the calculation of counterparty credit risk for SFTs
21.80

(1)
15% if bucket b and bucket c fall within bucket numbers 1 to 10;
(2)
0% if either of bucket b and bucket c is bucket 11;
(3)
75% if bucket b and bucket c are bucket numbers 12 and 13 (i.e. one is 
bucket 12, one is bucket 13); and
(4)
45% otherwise.
For delta commodity risk, 11 buckets that group commodities by common 
characteristics are set out in Table 11. 
21.81
For calculating weighted sensitivities, the risk weights for each bucket are set out 
in Table 11:
21.82
Delta commodity buckets and risk weights
Table 11
Bucket 
number
Commodity bucket
Examples of commodities allocated to
each commodity bucket (non-
exhaustive)
Risk weight
1
Energy - solid 
combustibles
Coal, charcoal, wood 
 
pellets , uranium
30%
2
Energy - liquid 
combustibles
Light-sweet crude oil; heavy crude oil; 
West Texas Intermediate (WTI) crude; 
Brent crude; etc (ie various types of 
crude oil)
Bioethanol; 
 
biodiesel ; etc (ie various 
biofuels)
Propane; ethane; gasoline; methanol; 
butane; etc (ie various petrochemicals)
Jet fuel; kerosene; gasoil; fuel oil; 
naphtha; heating oil; diesel etc (ie 
various refined fuels)
35%
3
Energy - electricity 
and carbon trading
Spot electricity; day-ahead electricity; 
peak electricity; off-peak electricity (ie 
various electricity types)
Certified emissions reductions; in-
delivery month EU allowance; 
Regional Greenhouse Gas Initiative 
CO2 allowance; renewable energy 
certificates; etc (ie various carbon 
trading emissions)
60%
4
Freight
Capesize; Panamax; Handysize; 
Supramax (ie various types of dry-bulk 
route)
Suezmax; Aframax; very large crude 
carriers (ie various liquid-bulk/gas 
shipping route)
80%
5
Metals – non-
precious
Aluminium; copper; lead; nickel; tin; 
zinc (ie various base metals)
Steel 
 
billet ; steel 
 
wire; steel coil ; steel 
scrap; steel rebar; iron ore; tungsten; 
vanadium; titanium; tantalum (ie steel 
raw materials)
40%
Cobalt; manganese; molybdenum (ie 
various minor metals)
6
Gaseous 
combustibles
Natural gas; liquefied natural gas
45%
7
Precious metals 
(including gold)
Gold; silver; platinum; palladium
20%
8
Grains and oilseed
Corn; wheat; soybean seed; soybean 
oil; soybean meal; oats; palm oil; 
canola; barley; rapeseed seed; 
rapeseed oil; rapeseed meal; red bean; 
sorghum; coconut oil; olive oil; peanut 
oil; sunflower oil; rice
35%
9
Livestock and dairy
Live cattle; feeder cattle; hog; poultry; 
lamb; fish; shrimp; milk; whey; eggs; 
butter; cheese
25%
10
Softs and other 
agriculturals
Cocoa; arabica coffee; robusta coffee; 
tea; citrus juice; orange juice; potatoes; 
sugar; cotton; wool; lumber; pulp; 
rubber
35%
11
Other commodity
Potash; fertilizer; phosphate rocks (ie 
various industrial materials)
Rare earths; terephthalic acid; flat glass
50%
For the purpose of aggregating commodity risk positions within a bucket using a
correlation parameter, the correlation parameter
 between two sensitivities
and
 within the same bucket, is set as follows, where:21

### MAR21.83 .94 address the calculation of counterparty credit risk for SFTs
21.83

(1)
 is equal to 1 where the two commodities of sensitivities k and l are
identical, and to the intra-bucket correlations in Table 12 otherwise, where, 
any two commodities are considered distinct commodities if in the market 
two contracts are considered distinct when the only difference between each 
other is the underlying commodity to be delivered. For example, WTI and 
Brent in bucket 2 (ie energy - liquid combustibles) would typically be treated 
as distinct commodities;
(2)
 is equal to 1 if the two tenors of the sensitivities k and l are identical,
and to 99.00% otherwise; and
(3)
 is equal to 1 if the two sensitivities are identical in the delivery
location of a commodity, and 99.90% otherwise.
Values of
 for intra-bucket correlations
Table 12
Bucket 
number
Commodity bucket
Correlation (
 )
1
Energy - Solid combustibles
55%
2
Energy - Liquid combustibles
95%
3
Energy - Electricity and carbon 
trading
40%
4
Freight
80%
5
Metals - non-precious
60%
6
Gaseous combustibles
65%
7
Precious metals (including gold)
55%
8
Grains and oilseed
45%
9
Livestock and dairy
15%
10
Softs and other agriculturals
40%
11
Other commodity
15%
Footnotes
For example, the correlation between the sensitivity to Brent, one-year 
tenor, for delivery in Le Havre and the sensitivity to WTI, five-year
tenor, for delivery in Oklahoma is
.
21
FAQ
For instruments with commodity spreads as underlying, are the spreads 
considered a risk factor, or does the instrument have to be 
decomposed? For example, if there is a swap on the spread between 
WTI and Brent, will delta on the spread be reported, or will delta of WTI 
and delta of Brent be reported individually?
Instruments with a spread as their underlying are considered sensitive 
to different risk factors. In the example cited, the swap will be sensitive 
to both WTI and Brent, each of which require a capital charge at the 
risk factor level (ie delta of WTI and delta of Brent). The correlation to 
aggregate capital charges is specified in 
.
MAR21.83
FAQ1
For determining whether the commodity correlation parameter (
 ) as set
out in Table 12 in 
(1)(a) should apply, this paragraph provides non-
MAR21.83
exhaustive examples of further definitions of distinct commodities as follows:

### MAR21.84 .94 address the calculation of counterparty credit risk for SFTs
21.84

(1)
For bucket 3 (energy – electricity and carbon trading):
(a)
Each time interval (i) at which the electricity can be delivered and (ii) 
that is specified in a contract that is made on a financial market is 
considered a distinct electricity commodity (eg peak and off-peak).
(b)
Electricity produced in a specific region (eg Electricity NE, Electricity SE 
or Electricity North) is considered a distinct electricity commodity.
(2)
For bucket 4 (freight):
(a)
Each combination of freight type and route is considered a distinct 
commodity.
(b)
Each week at which a good has to be delivered is considered a distinct 
commodity.
Foreign exchange risk buckets, risk weights and correlations
Footnotes
FAQ
For instruments with commodity spreads as underlying, are the spreads 
considered a risk factor, or does the instrument have to be 
decomposed? For example, if there is a swap on the spread between 
WTI and Brent, will delta on the spread be reported, or will delta of WTI 
and delta of Brent be reported individually?
Instruments with a spread as their underlying are considered sensitive 
to different risk factors. In the example cited, the swap will be sensitive 
to both WTI and Brent, each of which require a capital charge at the 
risk factor level (ie delta of WTI and delta of Brent). The correlation to 
aggregate capital charges is specified in 
.
MAR21.83
FAQ1
For aggregating delta commodity risk positions across buckets, the correlation 
parameter is set as follows:
21.85
(1)
20% if bucket b and bucket c fall within bucket numbers 1 to 10; and
(2)
0% if either bucket b or bucket c is bucket number 11.
An FX risk bucket is set for each exchange rate between the currency in which an 
instrument is denominated and the reporting currency.
21.86
A unique relative risk weight equal to 15% applies to all the FX sensitivities. 
21.87
For the specified currency pairs by the Basel Committee,22 and for currency pairs 
forming first-order crosses across these specified currency pairs,23 the above risk 
weight may at the discretion of the bank be divided by the square root of 2.

### MAR21.88 .94 address the calculation of counterparty credit risk for SFTs
21.88

Specified currency pairs by the Basel Committee are: USD/EUR, USD
/JPY, USD/GBP, USD/AUD, USD/CAD, USD/CHF, USD/MXN, USD/CNY, 
USD/NZD, USD/RUB, USD/HKD, USD/SGD, USD/TRY, USD/KRW, USD
/SEK, USD/ZAR, USD/INR, USD/NOK, USD/BRL.
22
For example, EUR/AUD is not among the selected currency pairs 
specified by the Basel Committee, but is a first-order cross of USD/EUR 
and USD/AUD.
23
Sensitivities-based method: definition of vega risk buckets, risk 
weights and correlations
For aggregating delta FX risk positions across buckets, the correlation parameter
is uniformly set to 60%.

### MAR21.89 .94 address the calculation of counterparty credit risk for SFTs
21.89

to 
 set out buckets, risk weights and correlation parameters 
MAR21.91
MAR21.95
to calculate vega risk capital requirement as set out in 
.
MAR21.4
21.90
The same bucket definitions for each risk class are used for vega risk as for delta 
risk.
21.91
For calculating weighted sensitivities for vega risk, the risk of market illiquidity is 
incorporated into the determination of vega risk, by assigning different liquidity 
horizons for each risk class as set out in Table 13. The risk weight for each risk 
class24 is also set out in Table 13.

### MAR21.92 .94 address the calculation of counterparty credit risk for SFTs
21.92

Regulatory liquidity horizon,
 , and risk weights per risk class
Table 13
Risk class
Risk weights
GIRR
60
100%
CSR non-securitisations
120
100%
CSR securitisations (CTP)
120
100%
CSR securitisations (non-CTP)
120
100%
Equity (large cap and indices)
20
77.78%
Equity (small cap and other 
sector)
60
100%
Commodity
120
100%
FX
40
100%
Footnotes
The risk weight for a given vega risk factor k
is determined by
,where
is set at 55%; and
is specified per risk class in Table 13.
24
FAQ
When applying risk weights for equity vega risk factors, does the 20 
days liquidity horizon apply to equities that are both large market cap 
and indices, or does it apply to equities that are either large market 
cap or indices? Similarly, does the 60 days liquidity horizon apply to 
equities that are both small market cap and other sector, or does it 
apply to equities that are either small market cap or other sector?
The 20-day liquidity horizon applies to vega risk factors that would be 
allocated to large market cap buckets (ie buckets 1 to 8) or to index 
buckets (ie buckets 12 and 13) as set out in 
. The 60-day 
MAR21.72
liquidity horizon applies to vega risk factors that would be allocated to 
small market cap buckets (ie buckets 9 and 10) or to the other sector 
bucket (ie bucket 11) as set out in 
.
MAR21.72
FAQ1
For aggregating vega GIRR risk positions within a bucket, the correlation
parameter
 is set as follows, where:

### MAR21.93 .94 address the calculation of counterparty credit risk for SFTs
21.93

(1)
 is equal to
 , where:
(a)
 is set at 1%;
(b)
 (respectively
 ) is the maturity of the option from which the vega
sensitivity
 (
 ) is derived, expressed as a number of years; and
(2)
 is equal to
 , where:
(a)
 is set at 1%; and
(b)
 (respectively
 ) is the maturity of the underlying of the option
from which the sensitivity
 (
 ) is derived, expressed as a number
of years after the maturity of the option.
For aggregating vega risk positions within a bucket of the other risk classes (ie
non-GIRR), the correlation parameter
 is set as follows, where:

### MAR21.94 .94 address the calculation of counterparty credit risk for SFTs
21.94

(1)
 is equal to the correlation that applies between the delta risk factors
that correspond to vega risk factors k and l. For instance, if k is the vega risk 
factor from equity option X and l is the vega risk factor from equity option Y
then
 is the delta correlation applicable between X and Y; and
(2)
 is defined as in 
:
MAR21.93
FAQ

## MAR21 .94 defines the vega correlation between risk factors k and l as

the product of the option maturity correlation (
) and the
delta correlation (
) that applies between the delta risk factors
that correspond to vega risk factors k and l. Please clarify the meaning 
of “delta risk factors that correspond to vega risk factors k and l”. In 
particular, besides the option maturity, should banks consider for CSR 
and commodity risk (i) the correlation across vega risk factors for the 
dimensions defined for vega for a given risk class only, or (ii) all 
dimensions of delta risk factors?
For CSR and commodity risks in 
 to 
 and 
, 
MAR21.9
MAR21.11
MAR21.13
if the vega risk factors are defined for a smaller number of dimensions 
than are defined for delta risk factors, only the dimensions that are 
defined both as a vega risk factor dimension and as a delta risk factor 
dimension for the relevant risk class need to be considered as a
correlation based on delta risk factors (
) in the calculation of
vega risk per 
. This means that the following dimensions are 
MAR21.94
considered:
for CSR non-securitisation risk: option maturity (
)  and underlying name (
);
for CSR securitisations (CTP) risk: option maturity (
)  and underlying name (
);
for CSR securitisation (non-CTP): option maturity (
)  and securitisation tranche (
); and
for commodity risk: option maturity (
)  and
commodity (
).
FAQ1
Sensitivities-based method: definition of curvature risk buckets, risk 
weights and correlations
For aggregating vega risk positions across different buckets within a risk class
(GIRR and non-GIRR), the same correlation parameters for
 , as specified for
delta correlations for each risk class in 
 to 
 are to be used for 
MAR21.39
MAR21.89
the aggregation of vega risk (eg
 = 50% is to be used for the aggregation of
vega risk sensitivities across different GIRR buckets).

### MAR21.95 .94 defines the vega correlation between risk factors k and l as
21.95

to 
 set out buckets, risk weights and correlation parameters 
MAR21.97
MAR21.101
to calculate curvature risk capital requirement as set out in 
.
MAR21.5
21.96
The delta buckets are replicated for the calculation of curvature risk capital 
requirement, unless specified otherwise in the preceding paragraphs within
to 
.
MAR21.8
MAR21.89

### MAR21.97 .94 defines the vega correlation between risk factors k and l as
21.97

For calculating the net curvature risk capital requirement
 for risk factor k for
FX and equity risk classes, the curvature risk weight, which is the size of a shock 
to the given risk factor, is a relative shift equal to the respective delta risk weight. 
For FX curvature, for options that do not reference a bank’s reporting currency (or 
base currency as set out in 
(b)) as an underlying, net curvature risk 
MAR21.14
charges (
 and
 ) may be divided by a scalar of 1.5. Alternatively, and
subject to supervisory approval, a bank may apply the scalar of 1.5 consistently to 
all FX instruments provided curvature sensitivities are calculated for all currencies, 
including sensitivities determined by shocking the reporting currency (or base 
currency where used) relative to all other currencies.

### MAR21.98 .94 defines the vega correlation between risk factors k and l as
21.98

For calculating the net curvature risk capital requirement
 for curvature risk
factor k for GIRR, CSR and commodity risk classes, the curvature risk weight is the 
parallel shift of all the tenors for each curve based on the highest prescribed delta 
risk weight for each bucket. For example, in the case of GIRR for a given currency 
(ie bucket), the risk weight assigned to 0.25-year tenor (ie the most punitive tenor 
risk weight) is applied to all the tenors simultaneously for each risk-free yield 
curve (consistent with a "translation", or "parallel shift" risk calculation).

### MAR21.99 .94 defines the vega correlation between risk factors k and l as
21.99

FAQ
In relation to the curvature risk capital requirement for the commodity 
risk class, 
 requires that the curvature risk weight is the 
MAR21.99
parallel shift of all the tenors for each curve based on the highest 
prescribed delta risk weight for each bucket. A parallel shift in MAR21.
implies that an additive shock (in absolute terms) is applied along 
99
the curve. However, 
 states that the shock applied to delta 
MAR21.23
commodity is a relative shock. How should the shock be applied to 
commodity curvature?
The sizes of upward and downward shocks applied to assess the net 
curvature risk capital requirement for a specific commodity´s curvature 
risk factor should be based on the risk weight connected to the 
curvature bucket where that commodity is classified, in accordance 
with 
 and 
. The same relative shocks should be 
MAR21.97
MAR21.82
applied to all curvature risk factors classified under the same bucket, 
defined along the dimension of the constructed curve (ie no term 
structure decomposition) per each commodity spot price, as described 
in 
(3). For example, the constructed curve for gold (with a 
MAR21.13
risk weight of 20%) would be shifted up by multiplying each tenor price 
by 1.2 and down by multiplying each tenor price by 0.8.
FAQ1
When calculating curvature capital requirements for the CSR risk 
classes as described in 
(1b), (1c) and (1d), are banks allowed 
MAR21.1
to floor the respective CSR curvature risk factors at zero when applying 
the downward shock to the CSR curvature risk factor?
When calculating curvature capital requirements for the CSR risk 
classes in accordance with 
 that would result in a negative 
MAR21.5
credit spread for 
, banks may floor the CSR curvature risk factor
to zero, after the application of the downward shock (ie 
). When
this approach is applied, banks must cap the risk weight (
) as
the difference between the level of the CSR curvature risk factor and
zero in calculating 
. However, banks must not cap the risk
weight 
when calculating 
.
FAQ2
For aggregating curvature risk positions within a bucket, the curvature risk
correlations
 are determined by squaring the corresponding delta correlation
parameters
. In a case where a curvature risk factor is defined differently than
the corresponding delta risk factor for a given risk class (ie for CSR non-
securitisations, CSR securitisations (CTP), CSR securitisations (non-CTP) and 
commodities as defined in 
 to 
), banks do not need to 
MAR21.9
MAR21.13
consider this delta risk factor dimension. For example, for CSR non-securitisations 
and CSR securitisations (CTP), consistent with 
 which defines a bucket 
MAR21.9
along one dimension (ie the relevant credit spread curve), the correlation
parameter
 as defined in 
 and 
 is not applicable to the 
MAR21.54
MAR21.55
curvature risk capital requirement calculation. Thus, the correlation parameter is 
determined by whether the two names of weighted sensitivities are the same. In
the formula in 
 and 
, the correlation parameters
 and
MAR21.54
MAR21.55
need not apply and only correlation parameter
 applies between
two weighted sensitivities within the same bucket. This correlation parameter 
should be squared. In applying the high and low correlations scenario set out in
, the curvature risk capital requirements are calculated by applying the 
MAR21.6
curvature correlation parameters
determined in this paragraph.

### MAR21.100 .94 defines the vega correlation between risk factors k and l as
21.100

For aggregating curvature risk positions across buckets, the curvature risk
correlations
 are determined by squaring the corresponding delta correlation
parameters
 . For instance, when aggregating
 and
 for the GIRR,
the correlation should be
 . In applying the high and low correlations
scenario set out in 
, the curvature risk capital requirements are 
MAR21.6
calculated by applying the curvature correlation parameters
 , (ie the square of
the corresponding delta correlation parameter).

### MAR21.101 .94 defines the vega correlation between risk factors k and l as
21.101


## MAR22 .94 defines the vega correlation between risk factors k and l as

Standardised approach: 
default risk capital 
requirement
This chapter sets out the calculation of the 
default risk capital requirement under the 
standardised approach for market risk.
Version effective as of
01 Jan 2023
Main concepts of default risk capital requirements
Instruments subject to the default risk capital requirement
Overview of DRC requirement calculation
The default risk capital (DRC) requirement is intended to capture jump-to-default 
(JTD) risk that may not be captured by credit spread shocks under the 
sensitivities-based method. DRC requirements provide some limited hedging 
recognition. In this chapter offsetting refers to the netting of exposures to the 
same obligor (where a short exposure may be subtracted in full from a long 
exposure) and hedging refers to the application of a partial hedge benefit from 
the short exposures (where the risk of long and short exposures in distinct 
obligors do not fully offset due to basis or correlation risks).

### MAR22.1 .94 defines the vega correlation between risk factors k and l as
22.1

The DRC requirement must be calculated for instruments subject to default risk: 
22.2
(1)
Non-securitisation portfolios
(2)
Securitisation portfolio (non-correlation trading portfolio, or non-CTP)
(3)
Securitisation (correlation trading portfolio, or CTP)
The following step-by-step approach must be followed for each risk class subject 
to default risk. The specific definition of gross JTD risk, net JTD risk, bucket, risk 
weight and the method for aggregation of DRC requirement across buckets are 
separately set out per each risk class in subsections in 
 to 
.
MAR22.9
MAR22.26

### MAR22.3 .94 defines the vega correlation between risk factors k and l as
22.3

(1)
The gross JTD risk of each exposure is computed separately.
(2)
With respect to the same obligator, the JTD amounts of long and short 
exposures are offset (where permissible) to produce net long and/or net 
short exposure amounts per distinct obligor.
(3)
Net JTD risk positions are then allocated to buckets.
(4)
Within a bucket, a hedge benefit ratio is calculated using net long and short 
JTD risk positions. This acts as a discount factor that reduces the amount of 
net short positions to be netted against net long positions within a bucket. A 
prescribed risk weight is applied to the net positions which are then 
aggregated.
(5)
Bucket level DRC requirements are aggregated as a simple sum across 
buckets to give the overall DRC requirement.
No diversification benefit is recognised between the DRC requirements for: 
22.4
(1)
non-securitisations;
(2)
securitisations (non-CTP); and
(3)
securitisations (CTP).
For traded non-securitisation credit and equity derivatives, JTD risk positions by 
individual constituent issuer legal entity should be determined by applying a look-
through approach.

### MAR22.5 .94 defines the vega correlation between risk factors k and l as
22.5

FAQ
What is the JTD equivalent when decomposing multiple underlying 
positions of a single security or product (eg index options) for purposes 
of the standardised approach?
The JTD equivalent is defined as the difference between the value of 
the security or product assuming that each single name referenced by 
the security or product, separately from the others, defaults (with zero 
recovery) and the value of the security or product assuming that none 
of the names referenced by the security or product default.
FAQ1
For the CTP, the capital requirement calculation includes the default risk for non-
securitisation hedges. These hedges must be removed from the calculation of 
default risk non-securitisation.

### MAR22.6 .94 defines the vega correlation between risk factors k and l as
22.6

Claims on sovereigns, public sector entities and multilateral development banks 
may, at national discretion, be subject to a zero default risk weight in line with
to 
 of the credit risk standard. National authorities may apply a 
CRE20.7
CRE20.15
non-zero risk weight to securities issued by certain foreign governments, 
including to securities denominated in a currency other than that of the issuing 
government.

### MAR22.7 .94 defines the vega correlation between risk factors k and l as
22.7

Default risk capital requirement for non-securitisations
Gross jump-to-default risk positions (gross JTD)
For claims on an equity investment in a fund that is subject to the treatment 
specified in 
(3) (ie treated as an unrated "other sector" equity), the 
MAR21.36
equity investment in the fund shall be treated as an unrated equity instrument. 
Where the mandate of that fund allows the fund to invest in primarily high-yield 
or distressed names, banks shall apply the maximum risk weight per Table 2 in
that is achievable under the fund's mandate (by calculating the 
MAR22.24
effective average risk weight of the fund when assuming that the fund invests
first in defaulted instruments to the maximum possible extent allowed under its 
mandate, and then in CCC-rated names to the maximum possible extent, and 
then B-rated, and then BB-rated). Neither offsetting nor diversification between 
these generated exposures and other exposures is allowed.

### MAR22.8 .94 defines the vega correlation between risk factors k and l as
22.8

FAQ
For equity investments in funds for which sensitivities-based method 
capital requirements are calculated under 
(3) (ie the “other 
MAR21.36
sector" equity treatment), may the mandate of the fund be used to 
determine the jump-to-default (JTD) of the fund for default risk?
No. In calculating the JTD, the LGD of equity investments in funds for 
which sensitivities-based method capital requirements are calculated 
under 
(3) should be 100%, consistent with the requirement in 
MAR21.36
to treat the equity investment as a position in an unrated 
MAR22.8
equity instrument.
FAQ1
The gross JTD risk position is computed exposure by exposure. For instance, if a 
bank has a long position on a bond issued by Apple, and another short position 
on a bond issued by Apple, it must compute two separate JTD exposures.

### MAR22.9 .94 defines the vega correlation between risk factors k and l as
22.9

For the purpose of DRC requirements, the determination of the long/short 
direction of positions must be on the basis of long or short with respect to 
whether the credit exposure results in a loss or gain in the case of a default.

### MAR22.10 .94 defines the vega correlation between risk factors k and l as
22.10

(1)
Specifically, a long exposure is defined as a credit exposure that results in a 
loss in the case of a default.
(2)
For derivative contracts, the long/short direction is also determined by 
whether the contract will result in a loss in the case of a default (ie long or
short position is not determined by whether the option or credit default 
swap (CDS), is bought or sold). Thus, for the purpose of DRC requirements, a 
sold put option on a bond is a long credit exposure, since a default results in 
a loss to the seller of the option.
The gross JTD is a function of the loss given default (LGD), notional amount (or 
face value) and the cumulative profit and loss (P&L) already realised on the 
position, where:

### MAR22.11 .94 defines the vega correlation between risk factors k and l as
22.11

(1)
notional is the bond-equivalent notional amount (or face value) of the 
position; and
(2)
P&L is the cumulative mark-to-market loss (or gain) already taken on the 
exposure. P&L is equal to the market value minus the notional amount, 
where the market value is the current market value of the position.
FAQ
What is the JTD equivalent when decomposing multiple underlying 
positions of a single security or product (eg index options) for purposes 
of the standardised approach?
The JTD equivalent is defined as the difference between the value of 
the security or product assuming that each single name referenced by 
the security or product, separately from the others, defaults (with zero 
recovery) and the value of the security or product assuming that none 
of the names referenced by the security or product default.
FAQ1
For calculating the gross JTD, LGD is set as follows:
22.12
(1)
Equity instruments and non-senior debt instruments are assigned an LGD of 
100%.
(2)
Senior debt instruments are assigned an LGD of 75%.
(3)
Covered bonds, as defined within 
, are assigned an LGD of 25%. 
MAR21.51
(4)
When the price of the instrument is not linked to the recovery rate of the 
defaulter (eg a foreign exchange-credit hybrid option where the cash flows 
are swap of cash flows, long EUR coupons and short USD coupons with a 
knockout feature that ends cash flows on an event of default of a particular 
obligor), there should be no multiplication of the notional by the LGD.
FAQ
For the purpose of market risk capital requirements, what are the credit 
spread risk capital requirements for Fannie Mae and Freddie Mac 
mortgage-backed security (MBS) bonds? What is the LGD for Fannie 
and Freddie MBS?
Non-tranched MBS issued by government sponsored-entities (GSEs), 
such as Fannie and Freddie, are assigned to bucket 2 (local 
government, government-backed non-financials, education, public 
administration) for credit spread risk with a risk weight of 1.0%.
In accordance with 
, the LGD for non-tranched MBS issued 
MAR22.12
by GSEs is 75% (ie the LGD assigned to senior debt instruments) unless 
the GSE security satisfies the requirements of footnote 15 to 
 
MAR21.51
for treatment of the security as a covered bond.
FAQ1
In calculating the JTD as set out in 
, the notional amount of an 
MAR22.11
instrument that gives rise to a long (short) exposure is recorded as a positive 
(negative) value, while the P&L loss (gain) is recorded as a negative (positive) 
value. If the contractual or legal terms of the derivative allow for the unwinding of 
the instrument with no exposure to default risk, then the JTD is equal to zero.

### MAR22.13 .94 defines the vega correlation between risk factors k and l as
22.13

The notional amount is used to determine the loss of principal at default, and the 
mark-to-market loss is used to determine the net loss so as to not double-count 
the mark-to-market loss already recorded in the market value of the position.

### MAR22.14 .94 defines the vega correlation between risk factors k and l as
22.14

(1)
For all instruments, the notional amount is the notional amount of the 
instrument relative to which the loss of principal is determined. Examples are 
as follows:
(a)
For a bond, the notional amount is the face value.
(b)
For credit derivatives, the notional amount of a CDS contract or a put 
option on a bond is the notional amount of the derivative contract.
(c)
In the case of a call option on a bond, the notional amount to be used 
in the JTD calculation is zero (since, in the event of default, the call 
option will not be exercised). In this case, a JTD would extinguish the call 
option's value and this loss would be captured through the mark-to-
market P&L term in the JTD calculation.
(2)
Table 1 illustrates examples of the notional amounts and market values for a 
long credit position with a mark-to-market loss to be used in the JTD 
calculation, where:
(a)
the bond-equivalent market value is an intermediate step in 
determining the P&L for derivative instruments;
(b)
the mark-to-market value of CDS or an option takes an absolute value; 
and
(c)
the strike amount of the bond option is expressed in terms of the bond 
price (not the yield).
Examples of components for a long credit position in the JTD 
calculation
Table 1
Instrument
Notional
Bond-equivalent
market value
P&L
Bond
Face value of 
bond
Market value of 
bond
Market value - 
face value
CDS
Notional of CDS
Notional of 
CDS +  mark-to-
market (MtM) 
value of CDS
- MtM value of 
CDS
Sold put option on 
a bond
Notional of 
option
Strike amount - | 
MtM value of 
option |
(Strike - | MtM 
value of option | 
) - Notional
Bought call option 
on a bond
0
MtM value of 
option
MtM value of 
option
P&L = bond-equivalent market value - notional.
With this representation of the P&L for a sold put option, a lower strike results
in a lower JTD loss.
Footnotes
FAQ
What is the JTD equivalent when decomposing multiple underlying 
positions of a single security or product (eg index options) for purposes 
of the standardised approach?
The JTD equivalent is defined as the difference between the value of 
the security or product assuming that each single name referenced by 
the security or product, separately from the others, defaults (with zero 
recovery) and the value of the security or product assuming that none 
of the names referenced by the security or product default.
FAQ1
Are convertible bonds to be treated the same way as vanilla bonds in 
computing the DRC requirement?
No. Banks should also consider the P&L of the equity optionality 
embedded within a convertible bond when computing its DRC 
requirement. A convertible bond can be decomposed into a vanilla 
bond and a long equity option. Hence, treating the convertible bond as 
a vanilla bond will potentially underestimate the JTD risk of the 
instrument.
FAQ2
To account for defaults within the one-year capital horizon, the JTD for all 
exposures of maturity less than one year and their hedges are scaled by a fraction 
of a year. No scaling is applied to the JTD for exposures of one year or greater.1 
For example, the JTD for a position with a six month maturity would be weighted 
by one-half, while the JTD for a position with a one year maturity would have no 
scaling applied to the JTD.

### MAR22.15 .94 defines the vega correlation between risk factors k and l as
22.15

Note that this paragraph refers to the scaling of gross JTD (ie not net 
JTD).
1
FAQ
states that for the standardised approach DRC requirement, 
MAR22.16
cash equity positions may be attributed a maturity of three months or 
a maturity of more than one year, at firms’ discretion. Such restrictions 
do not exist in 
 for the internal models approach, which allows 
MAR33
banks discretion to apply a 60-day liquidity horizon for equity sub-
portfolios. Furthermore, 
 states “... the JTD for all exposures 
MAR22.15
of maturity less than one year and their hedges are scaled by a fraction 
of a year”. Given the above-mentioned paragraphs, for purposes of the 
standardised approach DRC requirement, is a bank permitted to assign 
cash equities and equity derivatives such as index futures any maturity 
between three months and one year on a sub-portfolio basis in order 
to avoid broken hedges?
No. Such discretion is not permitted in the standardised approach. As 
required by 
, cash equity positions are assigned a maturity of 
MAR22.16
either more than one year or three months. There is no discretion 
permitted to assign cash equity positions to any maturity between 
three months and one year. In determining the offsetting criterion,
specifies that the maturity of the derivatives contract be 
MAR22.17
considered, not the maturity of the underlying instrument. 
 
MAR22.18
further states that the maturity weighting applied to the JTD for any 
product with a maturity of less than three months is floored at three 
months.
To illustrate how the standardised approach DRC requirement should 
be calculated with a simple hypothetical portfolio, consider equity 
index futures with one month to maturity and a negative market value 
of EUR 10 million (–EUR 10 million, maturity 1M), hedged with the 
underlying equity positions with a positive market value of EUR 10 
million (+EUR 10 million). Both positions in the example should be 
considered having a three-month maturity. Based on 
, which 
MAR22.15
requires maturity scaling, defined as a fraction of the year, of positions 
and their hedge, the JTD for the above trading portfolio would be 
calculated as follows: 1/4*10 – 1/4*10 = 0.
FAQ1
Cash equity positions (ie stocks) are assigned to a maturity of either more than 
one year or three months, at banks’ discretion. 
22.16
FAQ
states that for the standardised approach DRC requirement, 
MAR22.16
cash equity positions may be attributed a maturity of three months or 
a maturity of more than one year, at firms’ discretion. Such restrictions 
do not exist in 
 for the internal models approach, which allows 
MAR33
banks discretion to apply a 60-day liquidity horizon for equity sub-
portfolios. Furthermore, 
 states “... the JTD for all exposures 
MAR22.15
of maturity less than one year and their hedges are scaled by a fraction 
of a year”. Given the above-mentioned paragraphs, for purposes of the 
standardised approach DRC requirement, is a bank permitted to assign 
cash equities and equity derivatives such as index futures any maturity 
between three months and one year on a sub-portfolio basis in order 
to avoid broken hedges?
No. Such discretion is not permitted in the standardised approach. As 
required by 
, cash equity positions are assigned a maturity of 
MAR22.16
either more than one year or three months. There is no discretion 
permitted to assign cash equity positions to any maturity between 
three months and one year. In determining the offsetting criterion,
specifies that the maturity of the derivatives contract be 
MAR22.17
considered, not the maturity of the underlying instrument. 
 
MAR22.18
further states that the maturity weighting applied to the JTD for any 
product with maturity of less than three months is floored at three 
months.
To illustrate how the standardised approach DRC requirement should 
be calculated with a simple hypothetical portfolio, consider equity 
index futures with one month to maturity and a negative market value 
of EUR 10 million (–EUR 10 million, maturity 1M), hedged with the 
underlying equity positions with a positive market value of EUR 10 
million (+EUR 10 million). Both positions in the example should be 
considered having a three-month maturity. Based on 
, which 
MAR22.15
requires maturity scaling, defined as a fraction of the year, of positions 
and their hedge, the JTD for the above trading portfolio would be 
calculated as follows: 1/4*10 – 1/4*10 = 0.
FAQ1
For derivative exposures, the maturity of the derivative contract is considered in 
determining the offsetting criterion, not the maturity of the underlying 
instrument.

### MAR22.17 .94 defines the vega correlation between risk factors k and l as
22.17

Net jump-to-default risk positions (net JTD)
The maturity weighting applied to the JTD for any sort of product with a maturity 
of less than three months (such as short term lending) is floored at a weighting 
factor of one-fourth or, equivalently, three months (that means that the positions 
having shorter-than-three months remaining maturity would be regarded as
having a remaining maturity of three months for the purpose of the DRC 
requirement).

### MAR22.18 .94 defines the vega correlation between risk factors k and l as
22.18

FAQ
In the case where a total return swap (TRS) with a maturity of one 
month is hedged by the underlying equity, would the bank still need to 
compute a DRC requirement if there were sufficient legal terms on the 
TRS such that there is no settlement risk at swap maturity as the swap 
is terminated based on the executed price of the stock/bond hedge and 
any unwind of the TRS can be delayed (beyond the swap maturity 
date) in the event of hedge disruption until the stock/bond can be 
liquidated?
The net JTD for such a position would be zero. If the contractual/legal 
terms of the derivative allow for the unwinding of both legs of the 
position at the time of expiry of the first to mature with no exposure to 
default risk of the underlying credit beyond that point, then the JTD for 
the maturity-mismatched position is equal to zero.
FAQ1
Exposures to the same obligator may be offset as follows: 
22.19
(1)
The gross JTD risk positions of long and short exposures to the same obligor 
may be offset where the short exposure has the same or lower seniority 
relative to the long exposure. For example, a short exposure in an equity may 
offset a long exposure in a bond, but a short exposure in a bond cannot 
offset a long exposure in the equity.
(2)
For the purposes of determining whether a guaranteed bond is an exposure 
to the underlying obligor or an exposure to the guarantor, the credit risk 
mitigation requirements set out in 
 and 
 apply. 
CRE22.71
CRE22.73
Calculation of default risk capital requirement for non-securitisation
(3)
Exposures of different maturities that meet this offsetting criterion may be 
offset as follows.
(a)
Exposures with maturities longer than the capital horizon (one year) 
may be fully offset.
(b)
An exposure to an obligor comprising a mix of long and short 
exposures with a maturity less than the capital horizon (equal to one 
year) must be weighted by the ratio of the exposure’s maturity relative 
to the capital horizon. For example, with the one-year capital horizon, a 
three-month short exposure would be weighted so that its benefit 
against long exposures of longer-than-one-year maturity would be 
reduced to one quarter of the exposure size.
In the case of long and short offsetting exposures where both have a maturity 
under one year, the scaling can be applied to both the long and short exposures. 
22.20
Finally, the offsetting may result in net long JTD risk positions and net short JTD 
risk positions. The net long and net short JTD risk positions are aggregated 
separately as described below.

### MAR22.21 .94 defines the vega correlation between risk factors k and l as
22.21

For the default risk of non-securitisations, three buckets are defined as: 
22.22
(1)
corporates;
(2)
sovereigns; and
(3)
local governments and municipalities.
In order to recognise hedging relationship between net long and net short 
positions within a bucket, a hedge benefit ratio is computed as follows.
22.23
(1)
A simple sum of the net long JTD risk positions (not risk-weighted) must be 
calculated, where the summation is across the credit quality categories (ie 
rating bands). The aggregated amount is used in the numerator and 
denominator of the expression of the hedge benefit ratio (HBR) below.
(2)
A simple sum of the net (not risk-weighted) short JTD risk positions must be 
calculated, where the summation is across the credit quality categories (ie 
rating bands). The aggregated amount is used in the denominator of the 
expression of the HBR below.
(3)
The HBR is the ratio of net long JTD risk positions to the sum of net long JTD 
and absolute value of net short JTD risk positions:
For calculating the weighted net JTD, default risk weights are set depending on 
the credit quality categories (ie rating bands) for all three buckets (ie irrespective 
of the type of counterparty), as set out in Table 2:

### MAR22.24 .94 defines the vega correlation between risk factors k and l as
22.24

Default risk weights for non-securitisations by credit quality category
Table 2
Credit quality category
Default risk weight
AAA
0.5%
AA
2%
A
3%
BBB
6%
BB
15%
B
30%
CCC
50%
Unrated
15%
Defaulted
100%
FAQ
How are risk weights to be determined when external ratings assigned 
by credit rating agencies differ and when there are no external ratings 
available?
Consistent with the treatment of external ratings under the 
standardised approach to credit risk (see 
 and 
), if 
CRE21.10
CRE21.11
there are two ratings that map into different risk weights, the higher 
risk weight should be applied. If there are three or more ratings with 
different risk weights, the ratings corresponding to the two lowest risk 
weights should be referred to and the higher of those two risk weights 
will be applied.
Consistent with the treatment where there are no external ratings 
under the CVA risk chapter (see 
), where there are no 
MAR50.16
external ratings or where external ratings are not recognised within a 
jurisdiction, banks may, subject to supervisory approval:
-
for the purpose of assigning delta CSR non-securitisation risk 
weights, map the internal rating to an external rating, and assign a 
risk weight corresponding to either “investment grade” or “high-
yield” in the 
; 
MAR21.51
-
for the purpose of assigning default risk weights under the DRC 
requirement, map the internal rating to an external rating, and 
assign a risk weight corresponding to one of the seven external 
ratings in the table included in 
; or 
MAR22.24
-
apply the risk weights specified in 
 and 
 for 
MAR21.53
MAR22.24
unrated/non-rated categories.
FAQ1
The capital requirement for each bucket is to be calculated as the combination of 
the sum of the risk-weighted long net JTD, the HBR, and the sum of the risk-
weighted short net JTD, where the summation for each long net JTD and short 
net JTD is across the credit quality categories (ie rating bands). In the following 
formula, DRC stands for DRC requirement; and i refers to an instrument 
belonging to bucket b.

### MAR22.25 .94 defines the vega correlation between risk factors k and l as
22.25

Default risk capital requirement for securitisations (non-CTP)
Gross jump-to-default risk positions (gross JTD)
Net jump-to-default risk positions (net JTD)
No hedging is recognised between different buckets - the total DRC requirement 
for non-securitisations must be calculated as a simple sum of the bucket level 
capital requirements.

### MAR22.26 .94 defines the vega correlation between risk factors k and l as
22.26

For the computation of gross JTD on securitisations, the same approach must be 
followed as for default risk (non-securitisations), except that an LGD ratio is not 
applied to the exposure. Because the LGD is already included in the default risk 
weights for securitisations to be applied to the securitisation exposure (see 
below), to avoid double counting of LGD the JTD for securitisations is simply the 
market value of the securitisation exposure (ie the JTD for tranche positions is 
their market value).

### MAR22.27 .94 defines the vega correlation between risk factors k and l as
22.27

For the purposes of offsetting and hedging recognition for securitisations (non-
CTP), positions in underlying names or a non-tranched index position may be 
decomposed proportionately into the equivalent replicating tranches that span 
the entire tranche structure. When underlying names are treated in this way, they 
must be removed from the non-securitisation default risk treatment.

### MAR22.28 .94 defines the vega correlation between risk factors k and l as
22.28

For default risk of securitisations (non-CTP), offsetting is limited to a specific 
securitisation exposure (ie tranches with the same underlying asset pool). This 
means that:

### MAR22.29 .94 defines the vega correlation between risk factors k and l as
22.29

(1)
no offsetting is permitted between securitisation exposures with different 
underlying securitised portfolio (ie underlying asset pools), even if the 
attachment and detachment points are the same; and
(2)
no offsetting is permitted between securitisation exposures arising from 
different tranches with the same securitised portfolio.
Securitisation exposures that are otherwise identical except for maturity may be 
offset. The same offsetting rules for non-securitisations including scaling down 
positions of less than one year as set out in 
 through 
 apply 
MAR22.15
MAR22.18
to JTD risk positions for securitisations (non-CTP). Offsetting within a specific 
securitisation exposure is allowed as follows.

### MAR22.30 .94 defines the vega correlation between risk factors k and l as
22.30

Calculation of default risk capital requirement for securitisations (non-CTP)
(1)
Securitisation exposures that can be perfectly replicated through 
decomposition may be offset. Specifically, if a collection of long 
securitisation exposures can be replicated by a collection of short 
securitisation exposures, then the securitisation exposures may be offset.
(2)
Furthermore, when a long securitisation exposure can be replicated by a 
collection of short securitisation exposures with different securitised 
portfolios, then the securitisation exposure with the “mixed” securitisation 
portfolio may be offset by the combination of replicating securitisation 
exposures.
(3)
After the decomposition, the offsetting rules would apply as in any other 
case. As in the case of default risk (non-securitisations), long and short 
securitisation exposures should be determined from the perspective of long 
or short the underlying credit, eg the bank making losses on a long 
securitisation exposure in the event of a default in the securitised portfolio.
For default risk of securitisations (non-CTP), the buckets are defined as follows:
22.31
(1)
Corporates (excluding small and medium enterprises) – this bucket takes into 
account all regions.
(2)
Other buckets – these are defined along two dimensions:
(a)
Asset classes: the 11 asset classes are defined as asset-backed 
commercial paper; auto Loans/Leases; residential mortgage-backed 
securities (MBS); credit cards; commercial MBS; collateralised loan 
obligations; collateralised debt obligation (CDO)-squared; small and 
medium enterprises; student loans, other retail; and other wholesale.
(b)
Regions: the four regions are defined as Asia, Europe, North America 
and all other.
To assign a securitisation exposure to a bucket, banks must rely on a classification 
that is commonly used in the market for grouping securitisation exposures by 
type and region of underlying.

### MAR22.32 .94 defines the vega correlation between risk factors k and l as
22.32

(1)
The bank must assign each securitisation exposure to one and only one of 
the buckets above and it must assign all securitisations with the same type 
and region of underlying to the same bucket.
(2)
Any securitisation exposure that a bank cannot assign to a type or region of 
underlying in this fashion must be assigned to the “other bucket”.
Default risk capital requirement for securitisations (CTP)
Gross jump-to-default risk positions (gross JTD)
The capital requirement for default risk of securitisations (non-CTP) is determined 
using a similar approach to that for non-securitisations. The DRC requirement 
within a bucket is calculated as follows:

### MAR22.33 .94 defines the vega correlation between risk factors k and l as
22.33

(1)
The hedge benefit discount HBR, as defined in 
, is applied to net 
MAR22.23
short securitisation exposures in that bucket.
(2)
The capital requirement is calculated as in 
. 
MAR22.25
For calculating the weighted net JTD, the risk weights of securitisation exposures 
are defined by the tranche instead of the credit quality. The risk weight for 
securitisations (non-CTP) is applied as follows:

### MAR22.34 .94 defines the vega correlation between risk factors k and l as
22.34

(1)
The default risk weights for securitisation exposures are based on the 
corresponding risk weights for banking book instruments as set out in 
 
CRE40
to 
, with the following modification: the maturity component in the 
CRE44
banking book securitisation framework is set to zero (ie a one-year maturity 
is assumed) to avoid double-counting of risks in the maturity adjustment (of 
the banking book approach) since migration risk in the trading book will be 
captured in the credit spread capital requirement.
(2)
Following the corresponding treatment in the banking book, the hierarchy of 
approaches in determining the risk weights should be applied at the 
underlying pool level.
(3)
The capital requirement under the standardised approach for an individual 
cash securitisation position can be capped at the fair value of the transaction.
No hedging is recognised between different buckets. Therefore, the total DRC 
requirement for securitisations (non-CTP) must be calculated as a simple sum of 
the bucket-level capital requirements.

### MAR22.35 .94 defines the vega correlation between risk factors k and l as
22.35

For the computation of gross JTD on securitisations (CTP), the same approach 
must be followed as for default risk-securitisations (non-CTP) as described in
.
MAR22.27

### MAR22.36 .94 defines the vega correlation between risk factors k and l as
22.36

The gross JTD for non-securitisations (CTP) (ie single-name and index hedges) 
positions is defined as their market value. 
22.37
Net jump-to-default risk positions (net JTD)
Nth-to-default products should be treated as tranched products with attachment 
and detachment points defined below, where “Total names” is the total number 
of names in the underlying basket or pool:

### MAR22.38 .94 defines the vega correlation between risk factors k and l as
22.38

(1)
Attachment point = (N – 1) / Total names
(2)
Detachment point = N / Total names
Exposures that are otherwise identical except for maturity may be offset. The 
same concept of long and short positions from a perspective of loss or gain in 
the event of a default as set out in 
 and offsetting rules for non-
MAR22.10
securitisations including scaling down positions of less than one year as set out in
to 
 apply to JTD risk positions for securitisations (non-CTP).
MAR22.15
MAR22.18

### MAR22.39 .94 defines the vega correlation between risk factors k and l as
22.39

(1)
For index products, for the exact same index family (eg CDX.NA.IG), series 
(eg series 18) and tranche (eg 0–3%), securitisation exposures should be 
offset (netted) across maturities (subject to the offsetting allowance as 
described above).
(2)
Long and short exposures that are perfect replications through 
decomposition may be offset as follows. When the offsetting involves 
decomposing single name equivalent exposures, decomposition using a 
valuation model would be allowed in certain cases as follows. Such 
decomposition is the sensitivity of the security’s value to the default of the 
underlying single name obligor. Decomposition with a valuation model is 
defined as follows: a single name equivalent constituent of a securitisation 
(eg tranched position) is the difference between the unconditional value of 
the securitisation and the conditional value of the securitisation assuming 
that the single name defaults, with zero recovery, where the value is 
determined by a valuation model. In such cases, the decomposition into 
single-name equivalent exposures must account for the effect of marginal 
defaults of the single names in the securitisation, where in particular the sum 
of the decomposed single name amounts must be consistent with the 
undecomposed value of the securitisation. Further, such decomposition is 
restricted to vanilla securitisations (eg vanilla CDOs, index tranches or 
bespokes); while the decomposition of exotic securitisations (eg CDO 
squared) is prohibited.
Calculation of default risk capital requirement for securitisations (CTP)
(3)
Moreover, for long and short positions in index tranches, and indices (non-
tranched), if the exposures are to the exact same series of the index, then
offsetting is allowed by replication and decomposition. For instance, a long 
securitisation exposure in a 10–15% tranche vs combined short securitisation 
exposures in 10–12% and 12–15% tranches on the same index/series can be 
offset against each other. Similarly, long securitisation exposures in the 
various tranches that, when combined perfectly, replicate a position in the 
index series (non-tranched) can be offset against a short securitisation 
exposure in the index series if all the positions are to the exact same index 
and series (eg CDX.NA.IG series 18). Long and short positions in indices and 
single-name constituents in the index may also be offset by decomposition. 
For instance, single-name long securitisation exposures that perfectly 
replicate an index may be offset against a short securitisation exposure in 
the index. When a perfect replication is not possible, then offsetting is not 
allowed except as indicated in the next sentence. Where the long and short 
securitisation exposures are otherwise equivalent except for a residual 
component, the net amount must show the residual exposure. For instance, a 
long securitisation exposure in an index of 125 names, and short 
securitisation exposures of the appropriate replicating amounts in 124 of the 
names, would result in a net long securitisation exposure in the missing 
125th name of the index.
(4)
Different tranches of the same index or series may not be offset (netted), 
different series of the same index may not be offset, and different index 
families may not be offset.
For default risk of securitisations (CTP), each index is defined as a bucket of its 
own. A non-exhaustive list of indices include: CDX North America IG, iTraxx 
Europe IG, CDX HY, iTraxx XO, LCDX (loan index), iTraxx LevX (loan index), Asia 
Corp, Latin America Corp, Other Regions Corp, Major Sovereign (G7 and Western 
Europe) and Other Sovereign.

### MAR22.40 .94 defines the vega correlation between risk factors k and l as
22.40

Bespoke securitisation exposures should be allocated to the index bucket of the 
index they are a bespoke tranche of. For instance, the bespoke tranche 5% - 8% 
of a given index should be allocated to the bucket of that index.

### MAR22.41 .94 defines the vega correlation between risk factors k and l as
22.41

The default risk weights for securitisations applied to tranches are based on the 
corresponding risk weights for the banking book instruments, which is defined in 
a separate Basel Committee publication - Revisions to the Securitisations 
framework of 2014, 2016 and 2018, with the following modification: the maturity 
component in the banking book securitisation framework is set to zero, ie a one-
year maturity is assumed to avoid double-counting of risks in the maturity 
adjustment (of the banking book approach) since migration risk in the trading 
book will be captured in the credit spread capital requirement.

### MAR22.42 .94 defines the vega correlation between risk factors k and l as
22.42

For the non-tranched products, the same risk weights for non-securitisations as 
set out in 
 apply. For the tranched products, banks must derive the risk 
MAR22.24
weight using the banking book treatment as set out in 
.
MAR22.42

### MAR22.43 .94 defines the vega correlation between risk factors k and l as
22.43

Within a bucket (ie for each index) at an index level, the capital requirement for 
default risk of securitisations (CTP) is determined in a similar approach to that for 
non-securitisations.

### MAR22.44 .94 defines the vega correlation between risk factors k and l as
22.44

(1)
The hedge benefit ratio (HBR), as defined in 
, is modified and 
MAR22.23
applied to net short positions in that bucket as in the formula below, where 
the subscript ctp for the term HBR
 indicates that the HBR is determined 
ctp
using the combined long and short positions across all indices in the CTP (ie 
not only the long and short positions of the bucket by itself). The summation 
of risk-weighted amounts in the formula spans all exposures relating to the 
index (ie index tranche, bespoke, non-tranche index or single name).
(2)
A deviation from the approach for non-securitisations is that no floor at zero 
applies at the bucket level, and consequently, the DRC requirement at the
index level (
 ) can be negative.
The total DRC requirement for securitisations (CTP) is calculated by aggregating 
bucket level capital amounts as follows. For instance, if the DRC requirement for 
the index CDX North America IG is +100 and the DRC requirement for the index 
Major Sovereign (G7 and Western Europe) is -100, the total DRC requirement for
the CTP is
 .2

### MAR22.45 .94 defines the vega correlation between risk factors k and l as
22.45

Footnotes
The procedure for the
and
terms accounts for the
basis risk in cross index hedges, as the hedge benefit from cross-index 
short positions is discounted twice, first by the hedge benefit ratio HBR
in
, and again by the term 0.5 in the
equation.
2

## MAR23 .94 defines the vega correlation between risk factors k and l as

Standardised approach: 
residual risk add-on
This chapter sets out the calculation of residual 
risk add-on under the standardised approach for 
market risk.
Version effective as of
01 Jan 2023
Introduction
Instruments subject to the residual risk add-on
Footnotes
The residual risk add-on (RRAO) is to be calculated for all instruments bearing 
residual risk separately in addition to other components of the capital 
requirement under the standardised approach.

### MAR23.1 .94 defines the vega correlation between risk factors k and l as
23.1

Instruments with an exotic underlying and instruments bearing other residual 
risks are subject to the RRAO.
23.2
Instruments with an exotic underlying are trading book instruments with an 
underlying exposure that is not within the scope of delta, vega or curvature risk 
treatment in any risk class under the sensitivities-based method or default risk 
capital (DRC) requirements in the standardised approach.1

### MAR23.3 .94 defines the vega correlation between risk factors k and l as
23.3

Examples of exotic underlying exposures include: longevity risk, 
weather, natural disasters, future realised volatility (as an underlying 
exposure for a swap).
1
FAQ
Is future realised volatility considered an “exotic underlying” for the 
purpose of the RRAO?
Yes, future realised volatility is considered an exotic underlying for the 
purpose of the RRAO.
FAQ1
Instruments bearing other residual risks are those that meet criteria (1) and (2) 
below:
23.4
(1)
Instruments subject to vega or curvature risk capital requirements in the 
trading book and with pay-offs that cannot be written or perfectly replicated 
as a finite linear combination of vanilla options with a single underlying 
equity price, commodity price, exchange rate, bond price, credit default swap 
price or interest rate swap; or
(2)
Instruments which fall under the definition of the correlation trading 
portfolio (CTP) in 
, except for those instruments that are recognised 
MAR20.5
in the market risk framework as eligible hedges of risks within the CTP.
FAQ
Are bonds with multiple call dates considered instruments bearing 
other residual risks for the purpose of the RRAO?
Yes. Bonds with multiple call dates would be considered as instruments 
bearing other residual risks, as they are path-dependent options.
FAQ1
A non-exhaustive list of other residual risks types and instruments that may fall 
within the criteria set out in 
 include:
MAR23.4
23.5
(1)
Gap risk: risk of a significant change in vega parameters in options due to 
small movements in the underlying, which results in hedge slippage. 
Relevant instruments subject to gap risk include all path dependent options, 
such as barrier options, and Asian options as well as all digital options.
(2)
Correlation risk: risk of a change in a correlation parameter necessary for 
determining the value of an instrument with multiple underlyings. Relevant 
instruments subject to correlation risk include all basket options, best-of-
options, spread options, basis options, Bermudan options and quanto 
options.
(3)
Behavioural risk: risk of a change in exercise/prepayment outcomes such as 
those that arise in fixed rate mortgage products where retail clients may 
make decisions motivated by factors other than pure financial gain (such as 
demographical features and/or and other social factors). A callable bond 
may only be seen as possibly having behavioural risk if the right to call lies 
with a retail client.
When an instrument is subject to one or more of the following risk types, this by 
itself will not cause the instrument to be subject to the RRAO:
23.6
(1)
Risk from a cheapest-to-deliver option;
(2)
Smile risk: the risk of a change in an implied volatility parameter necessary 
for determining the value of an instrument with optionality relative to the 
implied volatility of other instruments optionality with the same underlying 
and maturity, but different moneyness;
(3)
Correlation risk arising from multi-underlying European or American plain 
vanilla options, and from any options that can be written as a linear 
combination of such options. This exemption applies in particular to the 
relevant index options;
Calculation of the residual risk add-on
(4)
Dividend risk arising from a derivative instrument whose underlying does not 
consist solely of dividend payments; and
(5)
Index instruments and multi-underlying options of which treatment for delta, 
vega or curvature risk are set out in 
 and 
. These are 
MAR21.31
MAR21.32
subject to the RRAO if they fall within the definitions set out in this chapter. 
For funds that are subject to the treatment specified in 
(3) (ie 
MAR21.36
treated as an unrated “other sector” equity), banks shall assume the fund is 
exposed to exotic underlying exposures, and to other residual risks, to the 
maximum possible extent allowed under the fund’s mandate.
In cases where a transaction exactly matches with a third-party transaction (ie a 
back-to-back transaction), the instruments used in both transactions must be 
excluded from the RRAO capital requirement. Any instrument that is listed and/or 
eligible for central clearing must be excluded from the RRAO for other residual 
risks as defined in 
. Any instrument that is listed and/or eligible for 
MAR23.4
central clearing with an exotic underlying must be included in the RRAO.

### MAR23.7 .94 defines the vega correlation between risk factors k and l as
23.7

FAQ
Can hedges (for example, dividend swaps hedging dividend risks) be 
excluded from the RRAO?
Hedges may be excluded from the RRAO only if the hedge exactly 
matches the trade (ie via a back-to-back transaction) as per 
. 
MAR23.7
For the example cited, dividend swaps should remain within the RRAO.
FAQ1
Can total return swap (TRS) products be netted with the underlying 
product(s) that drive the value of the TRS for the purposes of the RRAO?
As per 
, a TRS on an underlying product may be excluded 
MAR23.7
from the RRAO capital requirement if there is an equal and opposite 
exposure in the same TRS. If no exactly matching transaction exists, the 
entire notional of the TRS would be allocated to the RRAO.
FAQ2
The residual risk add-on must be calculated in addition to any other capital 
requirements within the standardised approach. The residual risk add-on is to be 
calculated as follows.

### MAR23.8 .94 defines the vega correlation between risk factors k and l as
23.8

Footnotes
(1)
The scope of instruments that are subject to the RRAO must not have an 
impact in terms of increasing or decreasing the scope of risk factors subject 
to the delta, vega, curvature or DRC treatments in the standardised approach.
(2)
The RRAO is the simple sum of gross notional amounts of the instruments 
bearing residual risks, multiplied by a risk weight.
(a)
The risk weight for instruments with an exotic underlying specified in
is 1.0%.
MAR23.3
(b)
The risk weight for instruments bearing other residual risks specified in
is 0.1%.
MAR23.4
2
Where the bank cannot satisfy the supervisor that the RRAO provides a 
sufficiently prudent capital charge, the supervisor will address any 
potentially under-capitalised risks by imposing a conservative 
additional capital charge under Pillar 2.
2

## MAR30 .94 defines the vega correlation between risk factors k and l as

Internal models approach: 
general provisions
This chapter sets out the general criteria for 
banks' use of the internal models approach.
Version effective as of
01 Jan 2023
More rigorous model approval process that 
enables supervisors to remove internal 
modelling permission for individual trading 
desks. Updated to take account of the revised 
implementation date announced on 27 March 
2020. FAQ on climate related financial risks 
added on 8 December 2022. Updated to 
incorporate the FAQ published on 5 July 2024.
General criteria
The use of internal models for the purposes of determining market risk capital 
requirements is conditional upon the explicit approval of the bank’s supervisory 
authority.

### MAR30.1 .94 defines the vega correlation between risk factors k and l as
30.1

The supervisory authority will only approve a bank's use of internal models to 
determine market risk capital requirements if, at a minimum:
30.2
(1)
the supervisory authority is satisfied that the bank's risk management system 
is conceptually sound and is implemented with integrity;
(2)
the bank has, in the supervisory authority's view, a sufficient number of staff 
skilled in the use of sophisticated models not only in the trading area but 
also in the risk control, audit and, if necessary, back office areas;
(3)
the bank's trading desk risk management model has, in the supervisory 
authority's judgement, a proven track record of reasonable accuracy in 
measuring risk;
(4)
the bank regularly conducts stress tests along the lines set out in 
 
MAR30.19
to 
; and
MAR30.23
(5)
the positions included in the bank's internal trading desk risk management 
models for determining minimum market risk capital requirements are held 
in trading desks that have been approved for the use of those models and 
that have passed the required tests described in 
.
MAR30.17
FAQ
How are the capital requirements for modellable risk factors (internally 
modelled capital charge, IMCC), stressed expected shortfall (SES) and 
default risk charge (DRC) calculated for reporting at the end of each 
quarter? More precisely, how are the results of backtesting at the 
trading desk level, the profit and loss attribution test (PLAT) at the 
trading desk level, and the risk factor eligibility test (RFET), as well as a 
change of a stress period and a reduced set of risk factors, considered 
in the calculation of the single risk figures used to determine the 
average capital numbers at the end of the quarter?
The scope of desks approved and eligible for the internal models 
approach (IMA) capital requirement calculation at the end of the 
quarter should be based on the results of backtesting and PLAT at the 
trading desk level. The PLAT and RFET must be performed quarterly. 
The Basel Framework does not specify in detail when these tests must 
be performed during the quarter but requires that “the bank’s risk 
management system is conceptually sound and is implemented with 
integrity”. Therefore, risk measures (Expected Shortfall (ES), SES, DRC) 
entering the 60-day (or 12-week) averages used for IMA capital 
computation at the end of the quarter should be calculated based on a 
stable set of desks. To calculate those risk measures, the results of the 
backtesting, PLAT and RFET should be used to update the set of eligible 
trading desks as well as the reduced set and the stressed period at the 
beginning of the 60-day (or 12-week) calculation period. To ensure 
representativeness, banks should ensure that the dates on which the 
backtesting and PLAT conclude and the RFET is performed are 
sufficiently close to the beginning of the 60-day (or 12-week) 
calculation period (the end of the previous quarter).
FAQ1
Supervisory authorities may insist on a period of initial monitoring and live 
testing of a bank’s internal trading desk risk management model before it is used 
for the purposes of determining the bank’s market risk capital requirements.

### MAR30.3 .94 defines the vega correlation between risk factors k and l as
30.3

The scope of trading portfolios that are eligible to use internal models to 
determine market risk capital requirements is determined based on a three-prong 
approach as follows:

### MAR30.4 .94 defines the vega correlation between risk factors k and l as
30.4

(1)
The bank must satisfy its supervisory authority that both the bank’s 
organisational infrastructure (including the definition and structure of 
trading desks) and its bank-wide internal risk management model meet 
qualitative evaluation criteria, as set out in 
 to 
.
MAR30.5
MAR30.16
(2)
The bank must nominate individual trading desks, as defined in 
 to 
MAR12.1
, for which the bank seeks model approval in order to use the 
MAR12.6
internal models approach (IMA).
(a)
The bank must nominate trading desks that it intends to be in-scope for 
model approval and trading desks that are out-of-scope for the use of 
the IMA. The bank must specify in writing the basis for these 
nominations.
(b)
The bank must not nominate trading desks to be out-of-scope for 
model approval due to capital requirements for a particular trading desk 
determined using the standardised approach being lower than those 
determined using the IMA.
(c)
The bank must use the standardised approach to determine the market 
risk capital requirements for trading desks that are out-of-scope for 
model approval. The positions in these out-of-scope trading desks are 
to be combined with all other positions that are subject to the 
standardised approach in order to determine the bank’s standardised 
approach capital requirements.
(d)
Trading desks that the bank does not nominate for model approval at 
the time of model approval will be ineligible to use the IMA for a period 
of at least one year from the date of the latest internal model approval.
(3)
The bank must receive supervisory approval to use the IMA on individual 
trading desks. Following the identification of eligible trading desks, this step 
determines which trading desks will be in-scope to use the IMA and which 
risk factors within in-scope trading desks are eligible to be included in the 
bank’s internal expected shortfall (ES) models to determine market risk 
capital requirements as set out in 
. 
MAR33
(a)
Each trading desk must satisfy profit and loss (P&L) attribution (PLA) 
tests on an ongoing basis to be eligible to use the IMA to determine 
market risk capital requirements. In order to conduct the PLA test, the 
bank must identify the set of risk factors to be used to determine its 
market risk capital requirements.
(b)
Each trading desk also must satisfy backtesting requirements on an 
ongoing basis to be eligible to use the IMA to determine market risk 
capital requirements as set out in 
 to 
.
MAR32.4
MAR32.19
(c)
Banks must conduct PLA tests and backtesting on a quarterly basis to 
update the eligibility and trading desk classification in PLA for trading 
desks in-scope to use the IMA.
(d)
The market risk capital requirements for risk factors that satisfy the risk 
factor eligibility test as set out in 
 to 
 must be 
MAR31.12
MAR31.24
determined using ES models as specified in 
 to 
.
MAR33.1
MAR33.15
(e)
The market risk capital requirements for risk factors that do not satisfy 
the risk factor eligibility test must be determined using stressed 
expected shortfall (SES) models as specified in 
 to 
. 
MAR33.16
MAR33.17
FAQ
The model approval process requires an overall assessment of a bank’s 
bank-wide internal risk capital model. Does the use of the term "bank-
wide” include a group of trading desks to be nominated as in-scope for 
model approval?
The term “bank-wide” is defined as pertaining to the group of trading 
desks that the bank nominates as in-scope in their application for the 
IMA.
FAQ1
As securitisations are out of scope for the IMA (IMA), are banks 
required to segregate desks to ensure securitisation and non-
securitisation products reside in different trading desks? If not, how 
should banks test model eligibility?
FAQ2
Qualitative standards
Securitisation positions are out of scope for IMA regulatory capital 
treatment, and as a result they are not taken into account for the 
model eligibility tests. This implies that banks are not allowed to 
include securitisations in trading desks for which they determine 
market risk capital requirements using the IMA. Securitisations must be 
included in trading desks for which capital requirements are 
determined using the standardised approach. Banks are allowed to also 
include hedging instruments in trading desks which include 
securitisations and are capitalised using the standardised approach.
In order to use the IMA to determine market risk capital requirements, the bank 
must have market risk management systems that are conceptually sound and 
implemented with integrity. Accordingly, the bank must meet the qualitative 
criteria set out below on an ongoing basis. Supervisors will assess that the bank 
has met the criteria before the bank is permitted to use the IMA.

### MAR30.5 .94 defines the vega correlation between risk factors k and l as
30.5

The bank must have an independent risk control unit that is responsible for the 
design and implementation of the bank’s market risk management system. The 
risk control unit should produce and analyse daily reports on the output of the 
trading desk’s risk management model, including an evaluation of the 
relationship between measures of risk exposure and trading limits. This risk 
control unit must be independent of business trading units and should report 
directly to senior management of the bank.

### MAR30.6 .94 defines the vega correlation between risk factors k and l as
30.6

The bank’s risk control unit must conduct regular backtesting and PLA 
assessments at the trading desk level. The bank must also conduct regular 
backtesting of its bank-wide internal models used for determining market risk 
capital requirements.

### MAR30.7 .94 defines the vega correlation between risk factors k and l as
30.7

A distinct unit of the bank that is separate from the unit that designs and 
implements the internal models must conduct the initial and ongoing validation 
of all internal models used to determine market risk capital requirements. The 
model validation unit must validate all internal models used for purposes of the 
IMA on at least an annual basis.

### MAR30.8 .94 defines the vega correlation between risk factors k and l as
30.8

The board of directors and senior management of the bank must be actively 
involved in the risk control process and must devote appropriate resources to risk 
control as an essential aspect of the business. In this regard, the daily reports 
prepared by the independent risk control unit must be reviewed by a level of
management with sufficient seniority and authority to enforce both reductions of 
positions taken by individual traders and reductions in the bank’s overall risk 
exposure.

### MAR30.9 .94 defines the vega correlation between risk factors k and l as
30.9

Internal models used to determine market risk capital requirements are likely to 
differ from those used by a bank in its day-to-day internal risk management 
functions. Nevertheless, the core design elements of both the market risk capital 
requirement model and the internal risk management model should be the same.

### MAR30.10 .94 defines the vega correlation between risk factors k and l as
30.10

(1)
Valuation models that are a feature of both models should be similar. These 
valuation models must be an integral part of the internal identification, 
measurement, management and internal reporting of price risks within the 
bank’s trading desks.
(2)
Internal risk management models should, at a minimum, be used to assess 
the risk of the positions that are subject to market risk capital requirements, 
although they may assess a broader set of positions.
(3)
The construction of a trading desk risk management model must be based 
on the methodologies used in the bank’s internal risk management model 
with regard to risk factor identification, parameter estimation and proxy 
concepts and deviate only if this is appropriate due to regulatory 
requirements. A bank’s market risk capital requirement model and its 
internal risk management model should address an identical set of risk 
factors.
A routine and rigorous programme of stress testing is required. The results of 
stress testing must be:
30.11
(1)
reviewed at least monthly by senior management;
(2)
used in the bank’s internal assessment of capital adequacy; and
(3)
reflected in the policies and limits set by the bank’s management and its 
board of directors.
Where stress tests reveal particular vulnerability to a given set of circumstances, 
the bank must take prompt action to mitigate those risks appropriately (eg by 
hedging against that outcome, reducing the size of the bank’s exposures or 
increasing capital).

### MAR30.12 .94 defines the vega correlation between risk factors k and l as
30.12

The bank must maintain a protocol for compliance with a documented set of 
internal manuals, policies, controls and procedures concerning the operation of 
the internal market risk management model. The bank’s risk management model 
must be well documented. Such documentation may include a comprehensive 
risk management manual that describes the basic principles of the risk 
management model and that provides a detailed explanation of the empirical 
techniques used to measure market risk.

### MAR30.13 .94 defines the vega correlation between risk factors k and l as
30.13

The bank must receive approval from its supervisory authority prior to 
implementing any significant changes to its internal models used to determine 
market risk capital requirements.

### MAR30.14 .94 defines the vega correlation between risk factors k and l as
30.14

The bank’s internal models for determining market risk capital requirements must 
address the full set of positions that are in the scope of application of the model. 
All models’ measurements of risk must be based on a sound theoretical basis, 
calculated correctly, and reported accurately.

### MAR30.15 .94 defines the vega correlation between risk factors k and l as
30.15

The bank’s internal audit and validation functions or external auditor must 
conduct an independent review of the market risk measurement system on at 
least an annual basis. The scope of the independent review must include both the 
activities of the business trading units and the activities of the independent risk 
control unit. The independent review must be sufficiently detailed to determine 
which trading desks are impacted by any failings. At a minimum, the scope of the 
independent review must include the following:

### MAR30.16 .94 defines the vega correlation between risk factors k and l as
30.16

(1)
the organisation of the risk control unit;
(2)
the adequacy of the documentation of the risk management model and 
process;
(3)
the accuracy and appropriateness of market risk management models 
(including any significant changes);
(4)
the verification of the consistency, timeliness and reliability of data sources 
used to run internal models, including the independence of such data 
sources;
(5)
the approval process for risk pricing models and valuation systems used by 
the bank’s front- and back-office personnel;
Model validation standards
(6)
the scope of market risks reflected in the trading desk risk management 
models;
(7)
the integrity of the management information system;
(8)
the accuracy and completeness of position data;
(9)
the accuracy and appropriateness of volatility and correlation assumptions;
(10)
the accuracy of valuation and risk transformation calculations;
(11)
the verification of trading desk risk management model accuracy through 
frequent backtesting and PLA assessments; and
(12)
the general alignment between the model to determine market risk capital 
requirements and the model the bank uses in its day-to-day internal 
management functions.
Banks must maintain a process to ensure that their internal models have been 
adequately validated by suitably qualified parties independent of the model 
development process to ensure that each model is conceptually sound and 
adequately reflects all material risks. Model validation must be conducted both 
when the model is initially developed and when any significant changes are made 
to the model. The bank must revalidate its models periodically, particularly when 
there have been significant structural changes in the market or changes to the 
composition of the bank’s portfolio that might lead to the models no longer 
being adequate. Model validation must include PLA and backtesting, and must, at 
a minimum, also include the following:

### MAR30.17 .94 defines the vega correlation between risk factors k and l as
30.17

(1)
Tests to demonstrate that any assumptions made within internal models are 
appropriate and do not underestimate risk. This may include reviewing the 
appropriateness of assumptions of normal distributions and any pricing 
models.
(2)
Further to the regulatory backtesting programmes, model validation must 
assess the hypothetical P&L (HPL) calculation methodology.
External validation
(3)
The bank must use hypothetical portfolios to ensure that internal models are 
able to account for particular structural features that may arise. For example, 
where the data history for a particular instrument does not meet the 
quantitative standards in 
 to 
 and the bank maps these 
MAR33.1
MAR33.12
positions to proxies, the bank must ensure that the proxies produce 
conservative results under relevant market scenarios, with sufficient 
consideration given to ensuring:
(a)
that material basis risks are adequately reflected (including mismatches 
between long and short positions by maturity or by issuer); and
(b)
that the models reflect concentration risk that may arise in an 
undiversified portfolio.
The model validation conducted by external auditors and/or supervisory 
authorities of a bank’s internal model to determine market risk capital 
requirements should, at a minimum, include the following steps:

### MAR30.18 .94 defines the vega correlation between risk factors k and l as
30.18

(1)
Verification that the internal validation processes described in 
 are 
MAR30.17
operating in a satisfactory manner;
(2)
Confirmation that the formulae used in the calculation process, as well as for 
the pricing of options and other complex instruments, are validated by a 
qualified unit, which in all cases should be independent from the bank’s 
trading area;
(3)
Confirmation that the structure of internal models is adequate with respect 
to the bank’s activities and geographical coverage;
(4)
Review of the results of both the bank’s backtesting of its internal models (ie 
comparison of value-at-risk with actual P&L and HPL) and its PLA process to 
ensure that the models provide a reliable measure of potential losses over 
time. On request, a bank should make available to its supervisory authority 
and/or to its external auditors the results as well as the underlying inputs to 
ES calculations and details of the PLA exercise; and
(5)
Confirmation that data flows and processes associated with the risk 
measurement system are transparent and accessible. On request and in 
accordance with procedures, the bank should provide its supervisory 
authority and its external auditors access to the models’ specifications and 
parameters.
Stress testing
Banks that use the IMA for determining market risk capital requirements must 
have in place a rigorous and comprehensive stress testing programme both at 
the trading desk level and at the bank-wide level.

### MAR30.19 .94 defines the vega correlation between risk factors k and l as
30.19

Banks’ stress scenarios must cover a range of factors that (i) can create 
extraordinary losses or gains in trading portfolios, or (ii) make the control of risk 
in those portfolios very difficult. These factors include low-probability events in all 
major types of risk, including the various components of market, credit and 
operational risks. A bank must design stress scenarios to assess the impact of 
such factors on positions that feature both linear and non-linear price 
characteristics (ie options and instruments that have option-like characteristics).

### MAR30.20 .94 defines the vega correlation between risk factors k and l as
30.20

Banks’ stress tests should be of a quantitative and qualitative nature, 
incorporating both market risk and liquidity risk aspects of market disturbances. 
30.21
(1)
Quantitative elements should identify plausible stress scenarios to which 
banks could be exposed.
(2)
Qualitatively, a bank’s stress testing programme should evaluate the capacity 
of the bank’s capital to absorb potential significant losses and identify steps 
the bank can take to reduce its risk and conserve capital.
Banks should routinely communicate results of stress testing to senior 
management and should periodically communicate those results to the bank’s 
board of directors.

### MAR30.22 .94 defines the vega correlation between risk factors k and l as
30.22

Banks should combine the use of supervisory stress scenarios with stress tests 
developed by the bank itself to reflect its specific risk characteristics. Stress 
scenarios may include the following:

### MAR30.23 .94 defines the vega correlation between risk factors k and l as
30.23

(1)
Supervisory scenarios requiring no simulations by the bank. A bank should 
have information on the largest losses experienced during the reporting 
period and may be required to make this available for supervisory review. 
Supervisors may compare this loss information to the level of capital 
requirements that would result from a bank’s internal measurement system. 
For example, the bank may be required to provide supervisory authorities 
with an assessment of how many days of peak day losses would have been 
covered by a given ES estimate.
(2)
Scenarios requiring a simulation by the bank. Banks should subject their 
portfolios to a series of simulated stress scenarios and provide supervisory 
authorities with the results. These scenarios could include testing the current 
portfolio against past periods of significant disturbance (eg the 1987 equity
crash, the Exchange Rate Mechanism crises of 1992 and 1993, the increase in 
interest rates in the first quarter of 1994, the 1998 Russian financial crisis, the 
2000 bursting of the technology stock bubble, the 2007–08 subprime 
mortgage crisis, or the 2011–12 Euro zone crisis) incorporating both the 
significant price movements and the sharp reduction in liquidity associated 
with these events. A second type of scenario would evaluate the sensitivity of 
the bank’s market risk exposure to changes in the assumptions about 
volatilities and correlations. Applying this test would require an evaluation of 
the historical range of variation for volatilities and correlations and 
evaluation of the bank’s current positions against the extreme values of the 
historical range. Due consideration should be given to the sharp variation 
that at times has occurred in a matter of days in periods of significant market 
disturbance. For example, the above-mentioned situations involved 
correlations within risk factors approaching the extreme values of 1 or –1 for 
several days at the height of the disturbance.
(3)
Bank-developed stress scenarios. In addition to the scenarios prescribed by 
supervisory authorities under 
(1), a bank should also develop its 
MAR30.23
own stress tests that it identifies as most adverse based on the 
characteristics of its portfolio (eg problems in a key region of the world 
combined with a sharp move in oil prices). A bank should provide 
supervisory authorities with a description of the methodology used to 
identify and carry out the scenarios as well as with a description of the 
results derived from these scenarios.

## MAR31 .94 defines the vega correlation between risk factors k and l as

Internal models approach: 
model requirements
This chapter sets out specification and model 
eligibility for risk factors per the internal models 
approach.
Version effective as of
01 Jan 2023
Updated to include the following FAQ: MAR31.
13 FAQ2.
Specification of market risk factors
An important part of a bank’s trading desk internal risk management model is the 
specification of an appropriate set of market risk factors. Risk factors are the 
market rates and prices that affect the value of the bank’s trading positions. The 
risk factors contained in a trading desk risk management model must be 
sufficient to represent the risks inherent in the bank’s portfolio of on- and off-
balance sheet trading positions. Although banks will have some discretion in 
specifying the risk factors for their internal models, the following requirements 
must be fulfilled.

### MAR31.1 .94 defines the vega correlation between risk factors k and l as
31.1

A bank’s market risk capital requirement models should include all risk factors 
that are used for pricing. In the event a risk factor is incorporated in a pricing 
model but not in the trading desk risk management model, the bank must 
support this omission to the satisfaction of its supervisory authority.

### MAR31.2 .94 defines the vega correlation between risk factors k and l as
31.2

A bank’s market risk capital requirement model must include all risk factors that 
are specified in the standardised approach for the corresponding risk class, as set 
out in 
 to 
. 
MAR20
MAR22

### MAR31.3 .94 defines the vega correlation between risk factors k and l as
31.3

(1)
In the event a standardised approach risk factor is not included in the market 
risk capital requirement model, the bank must support this omission to the 
satisfaction of its supervisory authority.
(2)
For securitised products, banks are prohibited from using internal models to 
determine market risk capital requirements. Banks must use the standardised 
approach to determine the market risk capital requirements for securitised 
products as set out in 
. Accordingly, a bank’s market risk capital 
MAR11.9
requirement model should not specify risk factors for securitisations as 
defined in 
 to 
.
MAR21.10
MAR21.11
A bank’s market risk capital requirement model and any stress scenarios 
calculated for non-modellable risk factors must address non-linearities for 
options and other relevant products (eg mortgage-backed securities), as well as 
correlation risk and relevant basis risks (eg basis risks between credit default 
swaps and bonds).

### MAR31.4 .94 defines the vega correlation between risk factors k and l as
31.4

A bank may use proxies for which there is an appropriate track record for their 
representation of a position (eg an equity index used as a proxy for a position in 
an individual stock). In the event a bank uses proxies, the bank must support their 
use to the satisfaction of the bank’s supervisory authority.

### MAR31.5 .94 defines the vega correlation between risk factors k and l as
31.5

For general interest rate risk, a bank must use a set of risk factors that 
corresponds to the interest rates associated with each currency in which the bank 
has interest rate sensitive on- or off-balance sheet trading positions.

### MAR31.6 .94 defines the vega correlation between risk factors k and l as
31.6

(1)
The trading desk risk management model must model the yield curve using 
one of a number of generally accepted approaches (eg estimating forward 
rates of zero coupon yields).
(2)
The yield curve must be divided into maturity segments in order to capture 
variation in the volatility of rates along the yield curve.
(3)
For material exposures to interest rate movements in the major currencies 
and markets, banks must model the yield curve using a minimum of six risk 
factors.
(4)
The number of risk factors used ultimately should be driven by the nature of 
the bank’s trading strategies. A bank with a portfolio of various types of 
securities across many points of the yield curve and that engages in complex 
arbitrage strategies would require the use of a greater number of risk factors 
than a bank with less complex portfolios.
The trading desk risk management model must incorporate separate risk factors 
to capture credit spread risk (eg between bonds and swaps). A variety of 
approaches may be used to reflect the credit spread risk arising from less-than-
perfectly correlated movements between government and other fixed income 
instruments, such as specifying a completely separate yield curve for non-
government fixed income instruments (eg swaps or municipal securities) or 
estimating the spread over government rates at various points along the yield 
curve.

### MAR31.7 .94 defines the vega correlation between risk factors k and l as
31.7

For exchange rate risk, the trading desk risk management model must 
incorporate risk factors that correspond to the individual foreign currencies in 
which the bank’s positions are denominated. Because the output of a bank’s risk 
measurement system will be expressed in the bank’s reporting currency, any net 
position denominated in a foreign currency will introduce foreign exchange risk. 
A bank must utilise risk factors that correspond to the exchange rate between the 
bank’s reporting currency and each foreign currency in which the bank has a 
significant exposure.

### MAR31.8 .94 defines the vega correlation between risk factors k and l as
31.8

For equity risk, a bank must utilise risk factors that correspond to each of the 
equity markets in which the bank holds significant positions.
31.9
Footnotes
(1)
At a minimum, a bank must utilise risk factors that reflect market-wide 
movements in equity prices (eg a market index). Positions in individual 
securities or in sector indices may be expressed in beta-equivalents relative 
to a market-wide index.
(2)
A bank may utilise risk factors that correspond to various sectors of the 
overall equity market (eg industry sectors or cyclical and non-cyclical 
sectors). Positions in individual securities within each sector may be 
expressed in beta-equivalents relative to a sector index.
(3)
A bank may also utilise risk factors that correspond to the volatility of 
individual equities.
(4)
The sophistication and nature of the modelling technique for a given market 
should correspond to the bank’s exposure to the overall market as well as 
the bank’s concentration in individual equities in that market.
For commodity risk, bank must utilise risk factors that correspond to each of the 
commodity markets in which the bank holds significant positions. 
31.10
(1)
For banks with relatively limited positions in commodity-based instruments, 
the bank may utilise a straightforward specification of risk factors. Such a 
specification could entail utilising one risk factor for each commodity price to 
which the bank is exposed (including different risk factors for different 
geographies where relevant).
(2)
For a bank with active trading in commodities, the bank’s model must 
account for variation in the convenience yield1 between derivatives positions 
such as forwards and swaps and cash positions in the commodity.
The convenience yield reflects the benefits from direct ownership of the 
physical commodity (eg the ability to profit from temporary market 
shortages). The convenience yield is affected both by market conditions 
and by factors such as physical storage costs.
1
For the risks associated with equity investments in funds:
31.11
Model eligibility of risk factors
(1)
For funds that meet the criterion set out in 
(5)(a) (ie funds with look-
RBC25.8
through possibility), banks must consider the risks of the fund, and of any 
associated hedges, as if the fund’s positions were held directly by the bank 
(taking into account the bank’s share of the equity of the fund, and any 
leverage in the fund structure). The bank must assign these positions to the 
trading desk to which the fund is assigned.
(2)
For funds that do not meet the criterion set out in 
(5)(a), but meet 
RBC25.8
both the criteria set out in 
(5)(b) (ie daily prices and knowledge of 
RBC25.8
the mandate of the fund), banks must use the standardised approach to 
calculate capital requirements for the fund.
A bank must determine which risk factors within its trading desks that have 
received approval to use the internal models approach as set out in 
 are 
MAR32
eligible to be included in the bank’s internal expected shortfall (ES) model for 
regulatory capital requirements as set out in 
. For a risk factor to be 
MAR33
classified as modellable by a bank, a necessary condition is that it passes the risk 
factor eligibility test (RFET). This test requires identification of a sufficient number 
of real prices that are representative of the risk factor. Collateral reconciliations or 
valuations cannot be considered real prices to meet the RFET. A price will be 
considered real if it meets at least one of the following criteria:

### MAR31.12 .94 defines the vega correlation between risk factors k and l as
31.12

(1)
It is a price at which the institution has conducted a transaction;
(2)
It is a verifiable price for an actual transaction between other arms-length 
parties;
(3)
It is a price obtained from a committed quote made by (i) the bank itself or 
(ii) another party. The committed quote must be collected and verified 
through a third-party vendor, a trading platform or an exchange; or
(4)
It is a price that is obtained from a third-party vendor, where:
(a)
the transaction or committed quote has been processed through the 
vendor;
(b)
the vendor agrees to provide evidence of the transaction or committed 
quote to supervisors upon request; or
(c)
the price meets any of the three criteria immediately listed in MAR31.12
(1) to 
(3).
MAR31.12
FAQ
What is the definition of a “committed quote” as referenced in MAR31.
?
12
A committed quote is a price from an arm’s length provider at which 
the provider of the quote must buy or sell the financial instrument.
FAQ1
Are all transactions and eligible committed quotes valid as real price 
observations, regardless of size?
Orderly transactions and eligible committed quotes with a non-
negligible volume, as compared to usual transaction sizes for the bank, 
reflective of normal market conditions can be generally accepted as 
valid.
FAQ2
To pass the RFET, a risk factor that a bank uses in an internal model must meet 
either of the following criteria on a quarterly basis. Any real price that is observed 
for a transaction should be counted as an observation for all of the risk factors for 
which it is representative.

### MAR31.13 .94 defines the vega correlation between risk factors k and l as
31.13

(1)
The bank must identify for the risk factor at least 24 real price observations 
per year (measured over the period used to calibrate the current ES model, 
with no more than one real price observation per day to be included in this 
count).2 3 Moreover, over the previous 12 months there must be no 90-day 
period in which fewer than four real price observations are identified for the 
risk factor (with no more than one real price observation per day to be 
included in this count). The above criteria must be monitored on a monthly 
basis; or
(2)
The bank must identify for the risk factor at least 100 real price observations 
over the previous 12 months (with no more than one real price observation 
per day to be included in this count).
Footnotes
When a bank uses data for real price observations from an external 
source, and those observations are provided with a time lag (eg data 
provided for a particular day is only made available a number of weeks 
later), the period used for the RFET may differ from the period used to 
calibrate the current ES model. The difference in periods used for the 
RFET and calibration of the ES model should not be greater than one 
month, ie the banks could use, for each risk factor, a one-year time 
period finishing up to one month before the RFET assessment instead 
of the period used to calibrate the current ES model.
2
In particular, a bank may add modellable risk factors, and replace non-
modellable risk factors by a basis between these additional modellable 
risk factors and these non-modellable risk factors. This basis will then 
be considered a non-modellable risk factor. A combination between 
modellable and non-modellable risk factors will be a non-modellable 
risk factor.
3
FAQ
When a bank uses external data to determine whether a risk factor 
passes the RFET, the period of observations used for the RFET may 
differ from the period of observations used to calibrate the bank’s 
expected shortfall model. According to footnote 2 in 
, the 
MAR31.13
difference in periods used for the RFET and calibration of the ES model 
should not be greater than one month. Does the requirement set out in 
footnote 2 of 
 apply when a bank uses internal data to 
MAR31.13
determine whether a risk factor passes the RFET?
Yes. Regardless of whether data is from internal or external sources, 
when a bank uses data for real price observations, the difference in 
periods used for the RFET and calibration of the ES model must not 
exceed one month.
FAQ1
Regarding the reform of benchmark reference rates, what guidance can 
the Committee provide on the count of real price observations for the 
risk factor eligibility test (RFET)?
Risk factors must have sufficient market liquidity, evidenced by records 
of trades, to be eligible for modelling. The replacement of risk factors 
due to benchmark rate reform could raise particular challenges for the 
count of real price observations for the risk factor eligibility test (RFET). 
Hence, when conducting the RFET for a new benchmark rate, banks 
can count both: (i) real price observations of the old benchmark rate
FAQ2
Footnotes
Bucketing approach for the RFET
(that has been replaced by the new benchmark rate) from before the 
discontinuation of the old benchmark rate; and (ii) real price 
observations of the new benchmark rate, until one year after the 
discontinuation of the old benchmark rate (eg in the UK, LIBOR 
discontinuation is expected to be 31 December 2021). In this context, 
discontinuation includes cessation of the old benchmark rate or an 
event whereby the old benchmark rate is deemed by its regulator to no 
longer be representative of the underlying market.
In order for a risk factor to pass the RFET, a bank may also count real price 
observations based on information collected from a third-party vendor provided 
all of the following criteria are met:

### MAR31.14 .94 defines the vega correlation between risk factors k and l as
31.14

(1)
The vendor communicates to the bank the number of corresponding real 
prices observed and the dates at which they have been observed.
(2)
The vendor provides, individually, a minimum necessary set of identifier 
information to enable banks to map real prices observed to risk factors.
(3)
The vendor is subject to an audit regarding the validity of its pricing 
information. The results and reports of this audit must be made available on 
request to the relevant supervisory authority and to banks as a precondition 
for the bank to be allowed to use real price observations collected by the 
third-party vendor. If the audit of a third-party vendor is not satisfactory to a 
supervisory authority, the supervisory authority may decide to prevent the 
bank from using data from this vendor.4
In this case, the bank may be permitted to use real price observations 
from this vendor for other risk factors.
4
A real price is representative for a risk factor of a bank where the bank is able to 
extract the value of the risk factor from the value of the real price. The bank must 
have policies and procedures that describe its mapping of real price observations 
to risk factors. The bank must provide sufficient information to its supervisory 
authorities in order to determine if the methodologies the bank uses are 
appropriate.

### MAR31.15 .94 defines the vega correlation between risk factors k and l as
31.15

Where a risk factor is a point on a curve or a surface (and other higher 
dimensional objects such as cubes), in order to count real price observations for 
the RFET, banks may choose from the following bucketing approaches:

### MAR31.16 .94 defines the vega correlation between risk factors k and l as
31.16

(1)
The 
. Under this approach, the bank must define the 
own bucketing approach
buckets it will use and meet the following requirements:
(a)
Each bucket must include only one risk factor, and all risk factors must 
correspond to the risk factors that are part of the risk-theoretical profit 
and loss (RTPL) of the bank for the purpose of the profit and loss (P&L) 
attribution (PLA) test.5
(b)
The buckets must be non-overlapping.
(2)
The 
. Under this approach, the bank must use 
regulatory bucketing approach
the following set of standard buckets as set out in Table 1.
(a)
For interest rate, foreign exchange and commodity risk factors with one 
maturity dimension (excluding implied volatilities) (t, where t is 
measured in years), the buckets in row (A) below must be used.
(b)
For interest rate, foreign exchange and commodity risk factors with 
several maturity dimensions (excluding implied volatilities) (t, where t is 
measured in years), the buckets in row (B) below must be used.
(c)
Credit spread and equity risk factors with one or several maturity 
dimensions (excluding implied volatilities) (t, where t is measured in 
years), the buckets in row (C) below must be used.
(d)
For any risk factors with one or several strike dimensions (delta, δ; ie the 
probability that an option is "in the money" at maturity), the buckets in 
row (D) below must be used.6
(e)
For expiry and strike dimensions of implied volatility risk factors 
(excluding those of interest rate swaptions), only the buckets in rows (C) 
and (D) below must be used.
(f)
For maturity, expiry and strike dimensions of implied volatility risk 
factors from interest rate swaptions, only the buckets in row (B), (C) and 
(D) below must be used.
Standard buckets for the regulatory bucketing approach
Table 1
Row
Bucket
1
2
3
4
5
6
7
8
9
(A) 0≤t<0.
75
0.75
≤t<1.5
1.5≤t<4 4≤t<7
7≤t<12 12≤t<18 18≤t<25 25≤t<35 35≤t<∞
(B) 0≤t<0.
75
0.75
≤t<4
4≤t<10 10≤t<18 18≤t<30 30≤t<∞
(C) 0≤t<1.5
1.5
≤t<3.5
3.5
≤t<7.5
7.5
≤t<15
15≤t<∞
(D) 0≤δ<0.
05
0.05
≤δ<0.
3
0.3
≤δ<0.7
0.7≤δ<0.
95
0.95
≤δ<1.00
Footnotes
Footnotes
The requirement to use the same buckets or segmentation of risk 
factors for the PLA test and the RFET recognises that there is a trade-
off in determining buckets for an ES model. The use of more granular 
buckets may facilitate a trading desk’s success in meeting the 
requirements of the PLA test, but additional granularity may challenge 
a bank’s ability to source a sufficient number of real observed prices 
per bucket to satisfy the RFET. Banks should consider this trade-off 
when designing their ES models.
5
For options markets where alternative definitions of moneyness are 
standard, banks shall convert the regulatory delta buckets to the 
market-standard convention using their own approved pricing models.
6
Banks may count all real price observations allocated to a bucket to assess 
whether it passes the RFET for any risk factors that belong to the bucket. A real 
price observation must be allocated to a bucket for which it is representative of 
any risk factors that belong to the bucket.

### MAR31.17 .94 defines the vega correlation between risk factors k and l as
31.17

As debt instruments mature, real price observations for those products that have 
been identified within the prior 12 months are usually still counted in the 
maturity bucket to which they were initially allocated per 
. When banks 
MAR31.17
no longer need to model a credit spread risk factor belonging to a given maturity 
bucket, banks are allowed to re-allocate the real price observations of this bucket 
to the adjacent (shorter) maturity bucket.7 A real price observation may only be 
counted in a single maturity bucket for the purposes of the RFET.

### MAR31.18 .94 defines the vega correlation between risk factors k and l as
31.18

For example, if a bond with an original maturity of four years, had a 
real price observation on its issuance date eight months ago, banks can 
opt to allocate the real price observation to the bucket associated with 
a maturity between 1.5 and 3.5 years instead of to the bucket 
associated with a maturity between 3.5 and 7.5 years to which it would 
normally be allocated.
7
Principles for the modellability of risk factors that pass the RFET
Where a bank uses a parametric function to represent a curve/surface and 
defines the function’s parameters as the risk factors in its risk measurement 
system, the RFET must be passed at the level of the market data used to calibrate 
the function’s parameters and not be passed directly at the level of these risk 
factor parameters (due to the fact that real price observations may not exist that 
are directly representative of these risk factors).

### MAR31.19 .94 defines the vega correlation between risk factors k and l as
31.19

A bank may use systematic credit or equity risk factors within its models that are 
designed to capture market-wide movements for a given economy, region or 
sector, but not the idiosyncratic risk of a specific issuer (the idiosyncratic risk of a 
specific issuer would be a non-modellable risk factor (NMRF) unless there are 
sufficient real price observations of that issuer). Real price observations of market 
indices or instruments of individual issuers may be considered representative for 
a systematic risk factor as long as they share the same attributes as the 
systematic risk factor.

### MAR31.20 .94 defines the vega correlation between risk factors k and l as
31.20

In addition to the approach set out in 
, where systematic risk factors of 
MAR31.20
credit or equity risk factors include a maturity dimension (eg a credit spread 
curve), one of the bucketing approaches set out above must be used for this 
maturity dimension to count “real” price observations for the RFET.

### MAR31.21 .94 defines the vega correlation between risk factors k and l as
31.21

Once a risk factor has passed the RFET, the bank should choose the most 
appropriate data to calibrate its model. The data used for calibration of the 
model does not need to be the same data used to pass the RFET.

### MAR31.22 .94 defines the vega correlation between risk factors k and l as
31.22

Once a risk factor has passed the RFET, the bank must demonstrate that the data 
used to calibrate its ES model are appropriate based on the principles contained 
in 
 to 
. Where a bank has not met these principles to the 
MAR31.25
MAR31.26
satisfaction of its supervisory authority for a particular risk factor, the supervisory 
authority may choose to deem the data unsuitable for use to calibrate the model 
and, in such case, the risk factor must be excluded from the ES model and subject 
to capital requirements as an NMRF.

### MAR31.23 .94 defines the vega correlation between risk factors k and l as
31.23

There may, on very rare occasions, be a valid reason why a significant number of 
modellable risk factors across different banks may become non-modellable due 
to a widespread reduction in trading activities (for instance, during periods of 
significant cross-border financial market stress affecting several banks or when 
financial markets are subjected to a major regime shift). One possible supervisory 
response in this instance could be to consider as modellable a risk factor that no 
longer passes the RFET. However, such a response should not facilitate a decrease 
in capital requirements. Supervisory authorities should only pursue such a 
response under the most extraordinary, systemic circumstances.

### MAR31.24 .94 defines the vega correlation between risk factors k and l as
31.24

Banks use many different types of models to determine the risks resulting from 
trading positions. The data requirements for each model may be different. For 
any given model, banks may use different sources or types of data for the model’
s risk factors. Banks must not rely solely on the number of observations of real 
prices to determine whether a risk factor is modellable. The accuracy of the 
source of the risk factor real price observation must also be considered.

### MAR31.25 .94 defines the vega correlation between risk factors k and l as
31.25

In addition to the requirements specified in 
 to 
, banks must 
MAR31.12
MAR31.23
apply the principles below to determine whether a risk factor that passed the 
RFET can be modelled using the ES model or should be subject to capital 
requirements as an NMRF. Banks are required to demonstrate to their supervisory 
authorities that these principles are being followed. Supervisory authorities may 
determine risk factors to be non-modellable in the event these principles are not 
applied.

### MAR31.26 .94 defines the vega correlation between risk factors k and l as
31.26

(1)
Principle one. The data used may include combinations of modellable risk 
factors. Banks often price instruments as a combination of risk factors. 
Generally, risk factors derived solely from a combination of modellable risk 
factors are modellable. For example, risk factors derived through multifactor 
beta models for which inputs and calibrations are based solely on 
modellable risk factors, can be classified as modellable and can be included 
within the ES model. A risk factor derived from a combination of modellable 
risk factors that are mapped to distinct buckets of a given curve/surface is 
modellable only if this risk factor also passes the RFET.
(a)
Interpolation based on combinations of modellable risk factors should 
be consistent with mappings used for PLA testing (to determine the 
RTPL) and should not be based on alternative, and potentially broader, 
bucketing approaches. Likewise, banks may compress risk factors into a 
smaller dimension of orthogonal risk factors (eg principal components) 
and/or derive parameters from observations of modellable risk factors, 
such as in models of stochastic implied volatility, without the 
parameters being directly observable in the market.
(b)
Subject to the approval of the supervisor, banks may extrapolate up to a 
reasonable distance from the closest modellable risk factor. The 
extrapolation should not rely solely on the closest modellable risk factor 
but on more than one modellable risk factor. In the event that a bank 
uses extrapolation, the extrapolation must be considered in the 
determination of the RTPL.
(2)
Principle two. The data used must allow the model to pick up both 
idiosyncratic and general market risk. General market risk is the tendency of 
an instrument’s value to change with the change in the value of the broader 
market, as represented by an appropriate index or indices. Idiosyncratic risk
is the risk associated with a particular issuance, including default provisions, 
maturity and seniority. The data must allow both components of market risk 
to be captured in any market risk model used to determine capital 
requirements. If the data used in the model do not reflect either idiosyncratic 
or general market risk, the bank must apply an NMRF charge for those 
aspects that are not adequately captured in its model.
(3)
Principle three. The data used must allow the model to reflect volatility and 
correlation of the risk positions. Banks must ensure that they do not 
understate the volatility of an asset (eg by using inappropriate averaging of 
data or proxies). Further, banks must ensure that they accurately reflect the 
correlation of asset prices, rates across yield curves and/or volatilities within 
volatility surfaces. Different data sources can provide dramatically different 
volatility and correlation estimates for asset prices. The bank should choose 
data sources so as to ensure that (i) the data are representative of real price 
observations; (ii) price volatility is not understated by the choice of data; and 
(iii) correlations are reasonable approximations of correlations among real 
price observations. Furthermore, any transformations must not understate 
the volatility arising from risk factors and must accurately reflect the 
correlations arising from risk factors used in the bank’s ES model.
(4)
Principle four. The data used must be reflective of prices observed and/or 
quoted in the market. Where data used are not derived from real price 
observations, the bank must demonstrate that the data used are reasonably 
representative of real price observations. To that end, the bank must 
periodically reconcile price data used in a risk model with front office and 
back office prices. Just as the back office serves to check the validity of the 
front office price, risk model prices should be included in the comparison. 
The comparison of front or back office prices with risk prices should consist 
of comparisons of risk prices with real price observations, but front office 
and back office prices can be used where real price observations are not 
widely available. Banks must document their approaches to deriving risk 
factors from market prices.
(5)
Principle five. The data used must be updated at a sufficient frequency. A 
market risk model may require large amounts of data, and it can be 
challenging to update such large data sets frequently. Banks should strive to 
update their model data as often as possible to account for frequent 
turnover of positions in the trading portfolio and changing market 
conditions. Banks should update data at a minimum on a monthly basis, but
preferably daily. Additionally, banks should have a workflow process for 
updating the sources of data. Furthermore, where the bank uses regressions 
to estimate risk factor parameters, these must be re-estimated on a regular 
basis, generally no less frequently than every two weeks. Calibration of 
pricing models to current market prices must also be sufficiently frequent, 
ideally no less frequent than the calibration of front office pricing models. 
Where appropriate, banks should have clear policies for backfilling and/or 
gap-filling missing data.
(6)
Principle six. The data used to determine stressed expected shortfall (ES
) 
R,S
must be reflective of market prices observed and/or quoted in the period of 
stress. The data for the ES
 model should be sourced directly from the 
R,S
historical period whenever possible. There are cases where the characteristics 
of current instruments in the market differ from those in the stress period. 
Nevertheless, banks must empirically justify any instances where the market 
prices used for the stress period are different from the market prices actually 
observed during that period. Further, in cases where instruments that are 
currently traded did not exist during a period of significant financial stress, 
banks must demonstrate that the prices used match changes in prices or 
spreads of similar instruments during the stress period.
In cases where banks do not sufficiently justify the use of current market 
data for products whose characteristics have changed since the stress period, 
the bank must omit the risk factor for the stressed period and meet the 
requirement of 
(2)(b) that the reduced set of risk factors explain 
MAR33.5
75% of the fully specified ES model. Moreover, if name-specific risk factors 
are used to calculate the ES in the actual period and these names were not 
available in the stressed period, there is a presumption that the idiosyncratic 
part of these risk factors are not in the reduced set of risk factors. Exposures 
for risk factors that are included in the current set but not in the reduced set 
need to be mapped to the most suitable risk factor of the reduced set for the 
purposes of calculating ES measures in the stressed period.
(7)
Principle seven. The use of proxies must be limited, and proxies must have 
sufficiently similar characteristics to the transactions they represent. Proxies
must be appropriate for the region, quality and type of instrument they are 
intended to represent. Supervisors will assess whether methods for 
combining risk factors are conceptually and empirically sound.
(a)
For example, the use of indices in a multifactor model must capture the 
correlated risk of the assets represented by the indices, and the 
remaining idiosyncratic risk must be demonstrably uncorrelated across 
different issuers. A multifactor model must have significant explanatory 
power for the price movements of assets and must provide an 
assessment of the uncertainty in the final outcome due to the use of a 
proxy. The coefficients (betas) of a multifactor model must be 
empirically based and must not be determined based on judgment. 
Instances where coefficients are set by judgment generally should be 
considered as NMRFs.
(b)
If risk factors are represented by proxy data in the current period ES 
model, the proxy data representation of the risk factor – not the risk 
factor itself – must be used in the RTPL unless the bank has identified 
the basis between the proxy and the actual risk factor and properly 
capitalised the basis either by including the basis in the ES model (if the 
risk factor is a modellable) or capturing the basis as a NMRF. If the 
capital requirement for the basis is properly determined, then the bank 
can choose to include in the RTPL either:
(i)
the proxy risk factor and the basis; or
(ii)
the actual risk factor itself.

## MAR32 .94 defines the vega correlation between risk factors k and l as

Internal models approach: 
backtesting and P&L 
attribution test requirements
This chapter sets out the profit and loss 
attribution test and backtesting requirements for 
banks that use the internal models approach.
Version effective as of
01 Jan 2023
Introduction
Backtesting requirements
As set out in 
, a bank that intends to use the internal models approach 
MAR30.4
(IMA) to determine market risk capital requirements for a trading desk must 
conduct and successfully pass backtesting at the bank-wide level and both the 
backtesting and profit and loss (P&L) attribution (PLA) test at the trading desk 
level as identified in 
(2).
MAR30.4

### MAR32.1 .94 defines the vega correlation between risk factors k and l as
32.1

For a bank to remain eligible to use the IMA to determine market risk capital 
requirements, a minimum of 10% of the bank’s aggregated market risk capital 
requirement must be based on positions held in trading desks that qualify for use 
of the bank’s internal models for market risk capital requirements by satisfying 
the backtesting and PLA test as set out in this chapter. This 10% criterion must be 
assessed by the bank on a quarterly basis when calculating the aggregate capital 
requirement for market risk according to 
.
MAR33.43

### MAR32.2 .94 defines the vega correlation between risk factors k and l as
32.2

The implementation of the backtesting programme and the PLA test must begin 
on the date that the internal models capital requirement becomes effective. 
32.3
(1)
For supervisory approval of a model, the bank must provide a one-year 
backtesting and PLA test report to confirm the quality of the model.
(2)
The bank’s supervisory authority may require backtesting and PLA test 
results prior to that date.
(3)
The bank’s supervisory authority will determine any necessary supervisory 
response to backtesting results based on the number of exceptions over the 
course of 12 months (ie 250 trading days) generated by the bank’s model.
(a)
Based on the assessment on the significance of exceptions, the 
supervisory authority may initiate a dialogue with the bank to determine 
if there is a problem with a bank’s model.
(b)
In the most serious cases, the supervisory authority will impose an 
additional increase in a bank’s capital requirement or disallow use of the 
model.
Backtesting requirements compare the value-at-risk (VaR) measure calibrated to 
a one-day holding period against each of the actual P&L (APL) and hypothetical 
P&L (HPL) over the prior 12 months. Specific requirements to be applied at the 
bank-wide level and trading desk level are set out below.

### MAR32.4 .94 defines the vega correlation between risk factors k and l as
32.4

Backtesting of the bank-wide risk model must be based on a VaR measure 
calibrated at a 99th percentile confidence level.

### MAR32.5 .94 defines the vega correlation between risk factors k and l as
32.5

(1)
An exception or an outlier occurs when either the actual loss or the 
hypothetical loss of the bank-wide trading book registered in a day of the 
backtesting period exceeds the corresponding daily VaR measure given by 
the model. As per 
, exceptions for actual losses are counted 
MAR99.8
separately from exceptions for hypothetical losses; the overall number of 
exceptions is the greater of these two amounts.
(2)
In the event either the P&L or the daily VaR measure is not available or 
impossible to compute, it will count as an outlier.
In the event an outlier can be shown by the bank to relate to a non-modellable 
risk factor, and the capital requirement for that non-modellable risk factor 
exceeds the actual or hypothetical loss for that day, it may be disregarded for the 
purpose of the overall backtesting process if the supervisory authority is notified 
accordingly and does not object to this treatment. In these cases, a bank must 
document the history of the movement of the value of the relevant non-
modellable risk factor and have supporting evidence that the non-modellable risk 
factor has caused the relevant loss.

### MAR32.6 .94 defines the vega correlation between risk factors k and l as
32.6

FAQ
Please confirm if this treatment applies to desk-level backtesting 
exceptions as well. Also, please confirm if the stressed capital add-on 
(SES) should be compared with the full loss amount or just the excess 
amount, ie the difference between APL/HPL and VaR.
If the backtesting exception at a desk-level test is being driven by a 
non-modellable risk factor that receives an SES capital requirement 
that is in excess of the maximum of the APL loss or HPL loss for that 
day, it is permitted to be disregarded for the purposes of the desk-level 
backtesting. The bank must be able to calculate a non-modellable risk 
factor capital requirement for the specific desk and not only for the 
respective risk factor across all desks.
For example, if the P&L for a desk is EUR –1.5 million and VaR is EUR 1 
million, a non-modellable risk factor capital requirement (at desk level) 
of EUR 0.8 million would not be sufficient to disregard an exception for 
the purpose of desk-level backtesting. The non-modellable risk factor 
capital requirement attributed to the standalone desk level (without 
VaR) must be greater than the loss of EUR 1.5 million in order to 
disregard an exception for the purpose of desk-level backtesting.
FAQ1
The scope of the portfolio subject to bank-wide backtesting should be updated 
quarterly based on the results of the latest trading desk-level backtesting, risk 
factor eligibility test and PLA tests.

### MAR32.7 .94 defines the vega correlation between risk factors k and l as
32.7

The framework for the supervisory interpretation of backtesting results for the 
bank-wide capital model encompasses a range of possible responses, depending 
on the strength of the signal generated from the backtesting. These responses 
are classified into three backtesting zones, distinguished by colours into a 
hierarchy of responses.

### MAR32.8 .94 defines the vega correlation between risk factors k and l as
32.8

(1)
Green zone. This corresponds to results that do not themselves suggest a 
problem with the quality or accuracy of a bank’s model.
(2)
Amber zone. This encompasses results that do raise questions in this regard, 
for which such a conclusion is not definitive.
(3)
Red zone. This indicates a result that almost certainly indicates a problem 
with a bank’s risk model.
These zones are defined according to the number of exceptions generated in the 
backtesting programme considering statistical errors as explained in 
 to 
MAR99.9
. Table 1 sets out boundaries for these zones and the presumptive 
MAR99.21
supervisory response for each backtesting outcome, based on a sample of 250 
observations.

### MAR32.9 .94 defines the vega correlation between risk factors k and l as
32.9

Backtesting zones
Table 1
Backtesting zone
Number of exceptions
Backtesting dependent 
multiplier (to be added to any 
qualitative add-on per MAR33.
)
44
Green
0
1
2
3
4
1.50
1.50
1.50
1.50
1.50
Amber
5
6
7
8
9
1.70
1.76
1.83
1.88
1.92
Red
10 or more
2.00
The backtesting green zone generally would not initiate a supervisory increase in 
capital requirements for backtesting (ie no backtesting add-on would apply).
32.10
Outcomes in the backtesting amber zone could result from either accurate or 
inaccurate models. However, they are generally deemed more likely for 
inaccurate models than for accurate models. Within the backtesting amber zone, 
the supervisory authority will impose a higher capital requirement in the form of 
a backtesting add-on. The number of exceptions should generally inform the size 
of any backtesting add-on, as set out in Table 1 of 
.
MAR32.9

### MAR32.11 .94 defines the vega correlation between risk factors k and l as
32.11

Backtesting at the trading desk level
A bank must also document all of the exceptions generated from its ongoing 
backtesting programme, including an explanation for each exception.

### MAR32.12 .94 defines the vega correlation between risk factors k and l as
32.12

A bank may also implement backtesting for confidence intervals other than the 
99th percentile, or may perform other statistical tests not set out in this standard. 
32.13
Besides a higher capital requirement for any outcomes that place the bank in the 
backtesting amber zone, in the case of severe problems with the basic integrity of 
the model, the supervisory authority may consider whether to disallow the bank’s 
use of the model for market risk capital requirement purposes altogether.

### MAR32.14 .94 defines the vega correlation between risk factors k and l as
32.14

If a bank’s model falls into the backtesting red zone, the supervisor will 
automatically increase the multiplication factor applicable to the bank’s model or 
may disallow use of the model.

### MAR32.15 .94 defines the vega correlation between risk factors k and l as
32.15

The performance of a trading desk’s risk management model will be tested 
through daily backtesting.
32.16
The backtesting assessment is considered to be complementary to the PLA 
assessment when determining the eligibility of a trading desk for the IMA. 
32.17
At the trading desk level, backtesting must compare each desk’s one-day VaR 
measure (calibrated to the most recent 12 months’ data, equally weighted) at 
both the 97.5th percentile and the 99th percentile, using at least one year of 
current observations of the desk’s one-day P&L.

### MAR32.18 .94 defines the vega correlation between risk factors k and l as
32.18

(1)
An exception or an outlier occurs when either the actual or hypothetical loss 
of the trading desk registered in a day of the backtesting period exceeds the 
corresponding daily VaR measure determined by the bank’s model. 
Exceptions for actual losses are counted separately from exceptions for 
hypothetical losses; the overall number of exceptions is the greater of these 
two amounts.
(2)
In the event either the P&L or the risk measure is not available or impossible 
to compute, it will count as an outlier.
Footnotes
PLA test requirements
FAQ
Are banks permitted to use volatility scaling of returns for the VaR 
calculation?
Volatility scaling of returns for VaR calculation at the discretion of the 
bank that results in a shorter observation period being used is not 
allowed. A bank may scale up the volatility of all observations for a 
selected (group of) risk factor(s) to reflect a recent stress period. The 
bank may use this scaled data to calculate future VaR and expected 
shortfall estimates only after ex ante notification of such a scaling to 
the supervisor.
FAQ1
If any given trading desk experiences either more than 12 exceptions at the 99th 
percentile or 30 exceptions at the 97.5th percentile in the most recent 12-month 
period, the capital requirement for all of the positions in the trading desk must be 
determined using the standardised approach.1

### MAR32.19 .94 defines the vega correlation between risk factors k and l as
32.19

Desks with exposure to issuer default risk must pass a two-stage 
approval process. First, the market risk model must pass backtesting 
and PLA. Conditional on approval of the market risk model, the desk 
may then apply for approval to model default risk. Desks that fail 
either test must be capitalised under the standardised approach.
1
The PLA test compares daily risk-theoretical P&L (RTPL) with the daily HPL for 
each trading desk. It intends to:
32.20
(1)
measure the materiality of simplifications in a banks’ internal models used 
for determining market risk capital requirements driven by missing risk 
factors and differences in the way positions are valued compared with their 
front office systems; and
(2)
prevent banks from using their internal models for the purposes of capital 
requirements when such simplifications are considered material.
The PLA test must be performed on a standalone basis for each trading desk in 
scope for use of the IMA. 
32.21
Definition of profits and losses used for the PLA test and backtesting
The RTPL is the daily trading desk-level P&L that is produced by the valuation 
engine of the trading desk’s risk management model.
32.22
(1)
The trading desk’s risk management model must include all risk factors that 
are included in the bank’s expected shortfall (ES) model with supervisory 
parameters and any risk factors deemed not modellable by the supervisory 
authority, and which are therefore not included in the ES model for 
calculating the respective regulatory capital requirement, but are included in 
non-modellable risk factors.
(2)
The RTPL must not take into account any risk factors that the bank does not 
include in its trading desk’s risk management model.
Movements in all risk factors contained in the trading desk’s risk management 
model should be included, even if the forecasting component of the internal 
model uses data that incorporates additional residual risk. For example, a bank 
using a multifactor beta-based index model to capture event risk might include 
alternative data in the calibration of the residual component to reflect potential 
events not observed in the name-specific historical time series. The fact that the 
name is a risk factor in the model, albeit modelled in a multifactor model 
environment, means that, for the purposes of the PLA test, the bank would 
include the actual return of the name in the RTPL (and in the HPL) and receive 
recognition for the risk factor coverage of the model.

### MAR32.23 .94 defines the vega correlation between risk factors k and l as
32.23

The PLA test compares a trading desk’s RTPL with its HPL. The HPL used for the 
PLA test should be identical to the HPL used for backtesting purposes. This 
comparison is performed to determine whether the risk factors included and the 
valuation engines used in the trading desk’s risk management model capture the 
material drivers of the bank’s P&L by determining if there is a significant degree 
of association between the two P&L measures observed over a suitable time 
period. The RTPL can differ from the HPL for a number of reasons. However, a 
trading desk risk management model should provide a reasonably accurate 
assessment of the risks of a trading desk to be deemed eligible for the internal 
models-based approach.

### MAR32.24 .94 defines the vega correlation between risk factors k and l as
32.24

The HPL must be calculated by revaluing the positions held at the end of the 
previous day using the market data of the present day (ie using static positions). 
As HPL measures changes in portfolio value that would occur when end-of-day 
positions remain unchanged, it must not take into account intraday trading nor 
new or modified deals, in contrast to the APL. Both APL and HPL include foreign 
denominated positions and commodities included in the banking book.

### MAR32.25 .94 defines the vega correlation between risk factors k and l as
32.25

Footnotes
PLA test data input alignment
Fees and commissions must be excluded from both APL and HPL as well as 
valuation adjustments for which separate regulatory capital approaches have 
been otherwise specified as part of the rules (eg credit valuation adjustment and 
its associated eligible hedges) and valuation adjustments that are deducted from 
Common Equity Tier 1 (eg the impact on the debt valuation adjustment 
component of the fair value of financial instruments must be excluded from these 
P&Ls).

### MAR32.26 .94 defines the vega correlation between risk factors k and l as
32.26

Any other market risk-related valuation adjustments, irrespective of the frequency 
by which they are updated, must be included in the APL while only valuation 
adjustments updated daily must be included in the HPL, unless the bank has 
received specific agreement to exclude them from its supervisory authority. 
Smoothing of valuation adjustments that are not calculated daily is not allowed. 
P&L due to the passage of time should be included in the APL and should be 
treated consistently in both HPL and RTPL.2

### MAR32.27 .94 defines the vega correlation between risk factors k and l as
32.27

Time effects can include various elements such as: the sensitivity to 
time, or theta effect (ie using mathematical terminology, the first-order 
derivative of the price relative to the time) and carry or costs of funding.
2
Valuation adjustments that the bank is unable to calculate at the trading desk 
level (eg because they are assessed in terms of the bank’s overall positions/risks 
or because of other constraints around the assessment process) are not required 
to be included in the HPL and APL for backtesting at the trading desk level, but 
should be included for bank-wide backtesting. To the satisfaction of its 
supervisory authority, the bank must provide support for valuation adjustments 
that are not computed at a trading desk level.

### MAR32.28 .94 defines the vega correlation between risk factors k and l as
32.28

Both APL and HPL must be computed based on the same pricing models (eg 
same pricing functions, pricing configurations, model parametrisation, market 
data and systems) as the ones used to produce the reported daily P&L.

### MAR32.29 .94 defines the vega correlation between risk factors k and l as
32.29

For the sole purpose of the PLA assessment, banks are allowed to align RTPL 
input data for its risk factors with the data used in HPL if these alignments are 
documented, justified to the supervisory authority and the requirements set out 
below are fulfilled:

### MAR32.30 .94 defines the vega correlation between risk factors k and l as
32.30

(1)
Banks must demonstrate that HPL input data can be appropriately used for 
RTPL purposes, and that no risk factor differences or valuation engine 
differences are omitted when transforming HPL input data into a format 
which can be applied to the risk factors used in RTPL calculation.
(2)
Any adjustment of RTPL input data must be properly documented, validated 
and justified to the supervisory authority.
(3)
Banks must have procedures in place to identify changes with regard to the 
adjustments of RTPL input data. Banks must notify the supervisory authority 
of any such changes.
(4)
Banks must provide assessments on the effect these input data alignments 
would have on the RTPL and the PLA test. To do so, banks must compare 
RTPL based on HPL-aligned market data with the RTPL based on market data 
without alignment. This comparison must be performed when designing or 
changing the input data alignment process and upon the request of the 
bank’s supervisory authority.
Adjustments to RTPL input data will be allowed when the input data for a given 
risk factor that is included in both the RTPL and the HPL differs due to different 
providers of market data sources or time fixing of market data sources, or 
transformations of market data into input data suitable for the risk factors of the 
underlying pricing models. These adjustments can be done either:

### MAR32.31 .94 defines the vega correlation between risk factors k and l as
32.31

(1)
by direct replacement of the RTPL input data (eg par rate tenor x, provider a) 
with the HPL input data (eg par rate tenor x, provider b); or
(2)
by using the HPL input data (eg par rate tenor x, provider b) as a basis to 
calculate the risk factor data needed in the RTPL/ES model (eg zero rate 
tenor x).
PLA test metrics
FAQ
In the event trading desks of a bank operate in different time zones 
compared to the location of the bank’s risk control department, data 
for risk modelling could be retrieved at different snapshot times 
compared to the data on which the desks’ front office P&L is based. Are 
banks permitted to align RTPL and HPL in terms of data snapshot 
times for these desks?
Banks are permitted to align the snapshot time used for the calculation 
of the RTPL of a desk to the snapshot time used for the derivation of its 
HPL.
FAQ1
If the HPL uses market data in a different manner to RTPL to calculate risk 
parameters that are essential to the valuation engine, these differences must be 
reflected in the PLA test and as a result in the calculation of HPL and RTPL. In this 
regard, HPL and RTPL are allowed to use the same market data only as a basis, 
but must use their respective methods (which can differ) to calculate the 
respective valuation engine parameters. This would be the case, for example, 
where market data are transformed as part of the valuation process used to 
calculate RTPL. In that instance, banks may align market data between RTPL and 
HPL pre-transformation but not post-transformation.

### MAR32.32 .94 defines the vega correlation between risk factors k and l as
32.32

Banks are not permitted to align HPL input data for risk factors with input data 
used in RTPL. Adjustments to RTPL or HPL to address residual operational noise 
are not permitted. Residual operational noise arises from computing HPL and 
RTPL in two different systems at two different points in time. It may originate 
from transitioning large portions of data across systems, and potential data 
aggregations may result in minor reconciliation gaps below tolerance levels for 
intervention; or from small differences in static/reference data and configuration.

### MAR32.33 .94 defines the vega correlation between risk factors k and l as
32.33

The PLA requirements are based on two test metrics:
32.34
(1)
the Spearman correlation metric to assess the correlation between RTPL and 
HPL; and
(2)
the Kolmogorov-Smirnov (KS) test metric to assess similarity of the 
distributions of RTPL and HPL.
To calculate each test metric for a trading desk, the bank must use the time series 
of the most recent 250 trading days of observations of RTPL and HPL.
32.35
Process for determining the Spearman correlation metric
Process for determining Kolmogorov-Smirnov test metrics
PLA test metrics evaluation
For a time series of HPL, banks must produce a corresponding time series of
ranks based on the size of the P&L
 . That is, the lowest value in the HPL
time series receives a rank of 1, the next lowest value receives a rank of 2 and so 
on.

### MAR32.36 .94 defines the vega correlation between risk factors k and l as
32.36

Similarly, for a time series of RTPL, banks must produce a corresponding time
series of ranks based on size
 .

### MAR32.37 .94 defines the vega correlation between risk factors k and l as
32.37

Banks must calculate the Spearman correlation coefficient of the two time series
of rank values of
 based on size using the following formula, where
and
 are the standard deviations of
 .

### MAR32.38 .94 defines the vega correlation between risk factors k and l as
32.38

The bank must calculate the empirical cumulative distribution function of RTPL. 
For any value of RTPL, the empirical cumulative distribution is the product of 
0.004 and the number of RTPL observations that are less than or equal to the 
specified RTPL.

### MAR32.39 .94 defines the vega correlation between risk factors k and l as
32.39

The bank must calculate the empirical cumulative distribution function of HPL. 
For any value of HPL, the empirical cumulative distribution is the product of 0.004 
and number of HPL observations that are less than or equal to the specified HPL.

### MAR32.40 .94 defines the vega correlation between risk factors k and l as
32.40

The KS test metric is the largest absolute difference observed between these two 
empirical cumulative distribution functions at any P&L value. 
32.41
Based on the outcome of the metrics, a trading desk is allocated to a PLA test red 
zone, an amber zone or a green zone as set out in Table 2.
32.42
(1)
A trading desk is in the PLA test green zone if both
(a)
the correlation metric is above 0.80; and
(b)
the KS distributional test metric is below 0.09 (p-value = 0.264).
(2)
A trading desk is in the PLA test red zone if the correlation metric is less than 
0.7 or if the KS distributional test metric is above 0.12 (p-value = 0.055).
(3)
A trading desk is in the PLA amber zone if it is allocated neither to the green 
zone nor to the red zone.
PLA test thresholds
Table 2
Zone
Spearman correlation
KS test
Amber zone thresholds
0.80
0.09 (p-value = 0.264)
Red zone thresholds
0.70
0.12 (p-value = 0.055)
If a trading desk is in the PLA test red zone, it is ineligible to use the IMA to 
determine market risk capital requirements and must be use the standardised 
approach.

### MAR32.43 .94 defines the vega correlation between risk factors k and l as
32.43

(1)
Risk exposures held by these ineligible trading desks must be included with 
the out-of-scope trading desks for purposes of determining capital 
requirement per the standardised approach.
(2)
A trading desk deemed ineligible to use the IMA must remain out-of-scope 
to use the IMA until:
(a)
the trading desk produces outcomes in the PLA test green zone; and
(b)
the trading desk has satisfied the backtesting exceptions requirements 
over the past 12 months.
If a trading desk is in the PLA test amber zone, it is not considered an out-of-
scope trading desk for use of the IMA.
32.44
Treatment for exceptional situations
(1)
If a trading desk is in the PLA test amber zone, it cannot return to the PLA 
test green zone until:
(a)
the trading desk produces outcomes in the PLA test green zone; and
(b)
the trading desk has satisfied its backtesting exceptions requirements 
over the prior 12 months.
(2)
Trading desks in the PLA test amber zone are subject to a capital surcharge 
as specified in 
.
MAR33.43
There may, on very rare occasions, be a valid reason why a series of accurate 
trading desk level-models across different banks will produce many backtesting 
exceptions or inadequately track the P&L produced by the front office pricing 
model (for instance, during periods of significant cross-border financial market 
stress affecting several banks or when financial markets are subjected to a major 
regime shift). One possible supervisory response in this instance would be to 
permit the relevant trading desks to continue to use the IMA but require each 
trading desk’s model to take account of the regime shift or significant market 
stress as quickly as practicable while maintaining the integrity of its procedures 
for updating the model. Supervisory authorities should only pursue such a 
response under the most extraordinary, systemic circumstances.

### MAR32.45 .94 defines the vega correlation between risk factors k and l as
32.45


## MAR33 .94 defines the vega correlation between risk factors k and l as

Internal models approach: 
capital requirements 
calculation
This chapter sets out the process by which 
capital requirements are calculated per the 
internal models approach.
Version effective as of
01 Jan 2023
Updated to include the following FAQ: MAR33.5 
FAQ4.
Calculation of expected shortfall
Banks will have flexibility in devising the precise nature of their expected shortfall 
(ES) models, but the following minimum standards will apply for the purpose of 
calculating market risk capital requirements. Individual banks or their supervisory 
authorities will have discretion to apply stricter standards.

### MAR33.1 .94 defines the vega correlation between risk factors k and l as
33.1

FAQ
Does the internal models approach (IMA) require all products to be 
simulated on full revaluation? Can a parametric approach be used on 
simple products, such as a forward rate agreement?
The IMA does not require all products to be simulated on full 
revaluation. Simplifications (eg sensitivities-based valuation) may be 
used provided the bank’s supervisor agrees that the method used is 
adequate for the instruments covered.
FAQ1
ES must be computed on a daily basis for the bank-wide internal models to 
determine market risk capital requirements. ES must also be computed on a daily 
basis for each trading desk that uses the internal models approach (IMA).

### MAR33.2 .94 defines the vega correlation between risk factors k and l as
33.2

In calculating ES, a bank must use a 97.5th percentile, one-tailed confidence level.
33.3
In calculating ES, the liquidity horizons described in 
 must be reflected 
MAR33.12
by scaling an ES calculated on a base horizon. The ES for a liquidity horizon must 
be calculated from an ES at a base liquidity horizon of 10 days with scaling 
applied to this base horizon result as expressed below, where:

### MAR33.4 .94 defines the vega correlation between risk factors k and l as
33.4

(1)
ES is the regulatory liquidity-adjusted ES;
(2)
T is the length of the base horizon, ie 10 days;
(3)
ES (P) is the ES at horizon T of a portfolio with positions P = (p ) with respect 
T
i
to shocks to all risk factors that the positions P are exposed to;
(4)
ES (P, j) is the ES at horizon T of a portfolio with positions P = (p ) with 
T
i
respect to shocks for each position p in the subset of risk factors Q(p , j), 
i
i 
with all other risk factors held constant;
(5)
the ES at horizon T, ES (P) must be calculated for changes in the risk factors, 
T
and ES (P, j) must be calculated for changes in the relevant subset Q(p , j) of 
T
i 
risk factors, over the time interval T without scaling from a shorter horizon;
(6)
Q(p , j) is the subset of risk factors for which liquidity horizons, as specified 
i 
in 
, for the desk where p is booked are at least as long as LH 
MAR33.12
i
j
according to the table below. For example, Q(p ,4) is the set of risk factors 
i
with a 60-day horizon and a 120-day liquidity horizon. Note that Q(p , j) is a 
i 
subset of Q(p , j-1);
i
(7)
the time series of changes in risk factors over the base time interval T may be 
determined by overlapping observations; and
(8)
LH is the liquidity horizon j, with lengths in the following table:
j
Liquidity horizons, j
Table 1
j
LHj
1
10
2
20
3
40
4
60
5
120
The ES measure must be calibrated to a period of stress.
33.5
(1)
Specifically, the ES measure must replicate an ES outcome that would be 
generated on the bank's current portfolio if the relevant risk factors were 
experiencing a period of stress. This is a joint assessment across all relevant 
risk factors, which will capture stressed correlation measures.
(2)
This calibration is to be based on an indirect approach using a reduced set of 
risk factors. Banks must specify a reduced set of risk factors that are relevant 
for their portfolio and for which there is a sufficiently long history of 
observations.
(a)
This reduced set of risk factors is subject to supervisory approval and 
must meet the data quality requirements for a modellable risk factor as 
outlined in 
 to 
.
MAR31.12
MAR31.24
(b)
The identified reduced set of risk factors must be able to explain a 
minimum of 75% of the variation of the full ES model (ie the ES of the 
reduced set of risk factors should be at least equal to 75% of the fully 
specified ES model on average measured over the preceding 12-week 
period).
FAQ
What indicator must be maximised for the identification of the stressed 
period?
The aggregate capital requirement for modellable risk factors (IMCC) 
as per 
 has to be maximised for the modellable risk factors.
MAR33.15
FAQ1
Is it correct that the reduced set of risk factors must explain a minimum 
of 75% of the variation of the full ES at the group level (ie top level) 
only and not at the desk level in order to be consistent with the 
stressed period selection performed at the group level?
Yes, the reduced set of risk factors must be able to explain a minimum 
of 75% of the variation of the full ES model at the group level for the 
aggregate of all desks with IMA model approval.
FAQ2
How should banks determine whether the ES measure calculated using 
a reduced set of risk factors explains at least 75% of the variation of 
the full ES model?
The average of the measurements of the ratio (ES using reduced set of 
risk factors and current period (ESR,C) to ES using full set of risk factors 
and current period (ESF,C)) over the preceding 12-week period must be 
at least 75%.
FAQ3
FAQ4
Regarding the reform of benchmark reference rates, what guidance can 
the Committee provide on the calculation of expected shortfall (ES) if 
the new benchmark rate was not available during a stress period for 
the purposes of 
?
MAR33
If the new benchmark rate is currently eligible for modelling according 
to MAR31 but was not available during the stress period, it may pose a 
challenge to banks calculating the expected shortfall (ES) for the 
current and stress period per 
. To address this, if the new 
MAR33
benchmark rate is eligible for modelling according to 
 but was 
MAR31
not available during the stress period, banks may use:
(i)
for the current period, the new benchmark rate in the full set of 
risk factors (ES
) and in the reduced set of risk factors (ES
); 
F,C
R,C
and
(ii)
for the stress period, the old benchmark rate in the reduced set of 
risk factors (ES
).
R,S
This interpretation does not annul the specification in 
(2) that 
MAR33.5
the reduced set is subject to supervisory approval and must meet the 
data quality requirements.
The ES for market risk capital purposes is therefore expressed as follows, where:
33.6
(1)
The ES for the portfolio using the above reduced set of risk factors (ES
), is 
R,S
calculated based on the most severe 12-month period of stress available 
over the observation horizon.
(2)
ES
 is then scaled up by the ratio of (i) the current ES using the full set of 
R,S
risk factors to (ii) the current ES measure using the reduced set of factors. For 
the purpose of this calculation, this ratio is floored at 1.
(a)
ES
 is the ES measure based on the current (most recent) 12-month 
F,C
observation period with the full set of risk factors; and
(b)
ES
 is the ES measure based on the current period with a reduced set 
R,C
of risk factors.
For measures based on stressed observations (ES
), banks must identify the 12-
R,S
month period of stress over the observation horizon in which the portfolio 
experiences the largest loss. The observation horizon for determining the most 
stressful 12 months must, at a minimum, span back to and include 2007. 
Observations within this period must be equally weighted. Banks must update 
their 12-month stressed periods at least quarterly, or whenever there are material 
changes in the risk factors in the portfolio. Whenever a bank updates its 12-
month stressed periods it must also update the reduced set of risk factors (as the 
basis for the calculations of E
 and E
) accordingly.
R,C
R,S

### MAR33.7 .94 defines the vega correlation between risk factors k and l as
33.7

For measures based on current observations (ES
), banks must update their data 
F,C
sets no less frequently than once every three months and must also reassess data 
sets whenever market prices are subject to material changes.

### MAR33.8 .94 defines the vega correlation between risk factors k and l as
33.8

(1)
This updating process must be flexible enough to allow for more frequent 
updates.
(2)
The supervisory authority may also require a bank to calculate its ES using a 
shorter observation period if, in the supervisor’s judgement; this is justified 
by a significant upsurge in price volatility. In this case, however, the period 
should be no shorter than six months.
No particular type of ES model is prescribed. Provided that each model used 
captures all the material risks run by the bank, as confirmed through profit and 
loss (P&L) attribution (PLA) tests and backtesting, and conforms to each of the 
requirements set out above and below, supervisors may permit banks to use 
models based on either historical simulation, Monte Carlo simulation, or other 
appropriate analytical methods.

### MAR33.9 .94 defines the vega correlation between risk factors k and l as
33.9

Banks will have discretion to recognise empirical correlations within broad 
regulatory risk factor classes (interest rate risk, equity risk, foreign exchange risk, 
commodity risk and credit risk, including related options volatilities in each risk 
factor category). Empirical correlations across broad risk factor categories will be 
constrained by the supervisory aggregation scheme, as described in 
 to 
MAR33.14
, and must be calculated and used in a manner consistent with the 
MAR33.15
applicable liquidity horizons, clearly documented and able to be explained to 
supervisors on request.

### MAR33.10 .94 defines the vega correlation between risk factors k and l as
33.10

Banks’ models must accurately capture the risks associated with options within 
each of the broad risk categories. The following criteria apply to the 
measurement of options risk:

### MAR33.11 .94 defines the vega correlation between risk factors k and l as
33.11

(1)
Banks’ models must capture the non-linear price characteristics of options 
positions.
(2)
Banks’ risk measurement systems must have a set of risk factors that 
captures the volatilities of the rates and prices underlying option positions, ie 
vega risk. Banks with relatively large and/or complex options portfolios must 
have detailed specifications of the relevant volatilities. Banks must model the 
volatility surface across both strike price and vertex (ie tenor).
As set out in 
, a scaled ES must be calculated based on the liquidity 
MAR33.4
horizon n defined below. n is calculated per the following conditions:
33.12
(1)
Banks must map each risk factor on to one of the risk factor categories 
shown below using consistent and clearly documented procedures.
(2)
The mapping of risk factors must be:
(a)
set out in writing;
(b)
validated by the bank’s risk management;
(c)
made available to supervisors; and
(d)
subject to internal audit.
(3)
n is determined for each broad category of risk factor as set out in Table 2. 
However, on a desk-by-desk basis, n can be increased relative to the values 
in the table below (ie the liquidity horizon specified below can be treated as 
a floor). Where n is increased, the increased horizon must be 20, 40, 60 or 
120 days and the rationale must be documented and be subject to 
supervisory approval. Furthermore, liquidity horizons should be capped at 
the maturity of the related instrument.
Liquidity horizon n by risk factor
Table 2
Risk factor category
n
Risk factor category
n
Interest rate: specified 
currencies - EUR, USD, GBP, 
AUD, JPY, SEK, CAD and 
domestic currency of a bank
10
Equity price (small cap): volatility
60
Interest rate: unspecified 
currencies
20
Equity: other types
60
Interest rate: volatility
60
Foreign exchange (FX) rate: 
specified currency pairs1
10
Interest rate: other types
60
FX rate: currency pairs
20
Credit spread: sovereign 
(investment grade, or IG)
20
FX: volatility 
40
Credit spread: sovereign (high 
yield, or HY)
40
FX: other types
40
Credit spread: corporate (IG)
40
Energy and carbon emissions 
trading price
20
Credit spread: corporate (HY)
60
Precious metals and non-
ferrous metals price
20
Credit spread: volatility
120
Other commodities price
60
Credit spread: other types
120
Energy and carbon emissions 
trading price: volatility
60
Precious metals and non-
ferrous metals price: volatility
60
Equity price (large cap)
10
Other commodities price: 
volatility
120
Footnotes
Equity price (small cap)
20
Commodity: other types
120
Equity price (large cap): 
volatility
20
USD/EUR, USD/JPY, USD/GBP, USD/AUD, USD/CAD, USD/CHF, USD
/MXN, USD/CNY, USD/NZD, USD/RUB, USD/HKD, USD/SGD, USD
/TRY, USD/KRW, USD/SEK, USD/ZAR, USD/INR, USD/NOK, USD/BRL, 
EUR/JPY, EUR/GBP, EUR/CHF and JPY/AUD. Currency pairs forming 
first-order crosses across these specified currency pairs are also subject 
to the same liquidity horizon.
1
FAQ
Please clarify the liquidity horizon to be used for equity dividends and 
equity repo risk factors.
The liquidity horizon for equity large cap repo and dividend risk factors 
is 20 days. All other equity repo and dividend risk factors are subject to 
a liquidity horizon of 60 days.
FAQ1
For mono-currency and cross-currency basis risk, should liquidity 
horizons of 10 days and 20 days for interest rate-specified currencies 
and unspecified currencies, respectively, be applied?
Yes.
FAQ2
To which liquidity horizon should inflation risk factors be assigned? 
Should the liquidity horizon for inflation risk factors be treated 
consistently with interest rates?
The liquidity horizon for inflation risk factors should be consistent with 
the liquidity horizons for interest rate risk factors for a given currency.
FAQ3
How must a bank treat risk factors in instruments that mature before 
the liquidity horizon of the respective risk factor prescribed in MAR33.12
?
If the maturity of the instrument is shorter than the respective liquidity 
horizon of the risk factor as prescribed in 
, the next longer 
MAR33.12
liquidity horizon length (out of the lengths of 10, 20, 40, 60 or 120 days 
as set out in the paragraph) compared with the maturity of the
FAQ4
Calculation of capital requirement for modellable risk factors
instrument itself must be used. For example, although the liquidity 
horizon for interest rate volatility is prescribed as 60 days, if an 
instrument matures in 30 days, a 40-day liquidity horizon would apply 
for the instrument’s interest rate volatility.
Which liquidity horizon should be mapped to multi-sector credit and 
equity indices (ie where different risk factor categories are involved)?
To determine the liquidity horizon of multi-sector credit and equity 
indices, the respective liquidity horizons of the underlying instruments 
must be used. A weighted average of liquidity horizons of the 
instruments contained in the index must be determined by multiplying 
the liquidity horizon of each individual instrument by its weight in the 
index (ie the weight used to construct the index) and summing across 
all instruments. The liquidity horizon of the index is the shortest 
liquidity horizon (out of 10, 20, 40, 60 and 120 days) that is equal to or 
longer than the weighted average liquidity horizon. For example, if the 
weighted average liquidity horizon is 12 days, the liquidity horizon of 
the index would be 20 days.
FAQ5
For those trading desks that are permitted to use the IMA, all risk factors that are 
deemed to be modellable must be included in the bank’s internal, bank-wide ES 
model. The bank must calculate its internally modelled capital requirement at the 
bank-wide level using this model, with no supervisory constraints on cross-risk 
class correlations (IMCC(C)).

### MAR33.13 .94 defines the vega correlation between risk factors k and l as
33.13

FAQ
Are banks permitted to not capitalise certain risks or risk factors via ES 
or stressed expected shortfall (SES) (as appropriate) as long as those 
risks or risk factors are not included in the model eligibility tests?
Banks design their own models for use under the IMA. As a result, they 
may exclude risk factors from IMA models as long as the bank’s 
supervisor does not conclude that the risk factor must be capitalised by 
either ES or SES. Moreover, at a minimum, the risk factors defined in
to 
 need to be covered in the IMA. If a risk factor is 
MAR31.1
MAR31.11
capitalised by neither ES nor SES, it is to be excluded from the 
calculation of risk-theoretical P&L.
FAQ1
The bank must calculate a series of partial ES capital requirements (ie all other 
risk factors must be held constant) for the range of broad regulatory risk classes 
(interest rate risk, equity risk, foreign exchange risk, commodity risk and credit 
spread risk). These partial, non-diversifiable (constrained) ES values (IMCC(C )) will 
i
then be summed to provide an aggregated risk class ES capital requirement.

### MAR33.14 .94 defines the vega correlation between risk factors k and l as
33.14

The aggregate capital requirement for modellable risk factors (IMCC) is based on 
the weighted average of the constrained and unconstrained ES capital 
requirements, where:

### MAR33.15 .94 defines the vega correlation between risk factors k and l as
33.15

(1)
The stress period used in the risk class level ES
 should be the same as 
R,S,i
that used to calculate the portfolio-wide ES
.
R,S
(2)
Rho (ρ) is the relative weight assigned to the firm’s internal model. The value 
of ρ is 0.5.
(3)
B stands for broad regulatory risk classes as set out in 
.
MAR33.14
FAQ
To calculate the aggregate capital requirement for modellable risk 
factors (internally modelled capital charge, IMCC) up to 63 daily ES 
calculations would be necessary if each ES measure were required to 
be calculated daily. Is it permissible to calculate some of the ES 
measures weekly or must all measures be calculated daily?
The formula specified in 
,
MAR33.15
, can be rewritten as
with
. While ES
 , ES
 and ES
 must be 
 
R,S
F,C
R,C
calculated daily, it is generally acceptable that the ratio of undiversified
IMCC(C) to diversified IMCC(C),
, may be calculated
on a weekly basis.
By defining
as
the formula for
the calculation of IMCC can be rearranged, leading to the following
expression of IMCC:
. Hence, IMCC can be
calculated as a multiple of IMCC(C), where IMCC(C) is calculated daily 
and the multiplier
is updated weekly.
Banks must have procedures and controls in place to ensure that the 
weekly calculation of the “undiversified IMCC(C) to diversified IMCC(C)” 
ratio does not lead to a systematic underestimation of risks relative to 
daily calculation. Banks must be in a position to switch to daily 
calculation upon supervisory direction.
FAQ1
Calculation of capital requirement for non-modellable risk factors
Capital requirements for each non-modellable risk factor (NMRF) are to be 
determined using a stress scenario that is calibrated to be at least as prudent as 
the ES calibration used for modelled risks (ie a loss calibrated to a 97.5% 
confidence threshold over a period of stress). In determining that period of stress, 
a bank must determine a common 12-month period of stress across all NMRFs in 
the same risk class. Subject to supervisory approval, a bank may be permitted to 
calculate stress scenario capital requirements at the bucket level (using the same 
buckets that the bank uses to disprove modellability, per 
) for risk 
MAR31.16
factors that belong to curves, surfaces or cubes (ie a single stress scenario capital 
requirement for all the NMRFs that belong to the same bucket).

### MAR33.16 .94 defines the vega correlation between risk factors k and l as
33.16

(1)
For each NMRF, the liquidity horizon of the stress scenario must be the 
greater of the liquidity horizon assigned to the risk factor in 
 and 
MAR33.12
20 days. The bank’s supervisory authority may require a higher liquidity 
horizon.
(2)
For NMRFs arising from idiosyncratic credit spread risk, banks may apply a 
common 12-month stress period. Likewise, for NMRFs arising from 
idiosyncratic equity risk arising from spot, futures and forward prices, equity 
repo rates, dividends and volatilities, banks may apply a common 12-month 
stress scenario. Additionally, a zero correlation assumption may be used 
when aggregating gains and losses provided the bank conducts analysis to 
demonstrate to its supervisor that this is appropriate. 2 Correlation or 
diversification effects between other non-idiosyncratic NMRFs are 
recognised through the formula set out in 
.
MAR33.17
(3)
In the event that a bank cannot provide a stress scenario which is acceptable 
for the supervisor, the bank will have to use the maximum possible loss as 
the stress scenario.
Footnotes
The tests are generally done on the residuals of panel regressions 
where the dependent variable is the change in issuer spread while the 
independent variables can be either a change in a market factor or a 
dummy variable for sector and/or region. The assumption is that the 
data on the names used to estimate the model suitably proxies the 
names in the portfolio and the idiosyncratic residual component 
captures the multifactor-name basis. If the model is missing systematic 
explanatory factors or the data suffers from measurement error, then 
the residuals would exhibit heteroscedasticity (which can be tested via 
White, Breuche Pagan tests etc) and/or serial correlation (which can be 
tested with Durbin Watson, Lagrange multiplier (LM) tests etc) and/or 
cross-sectional correlation (clustering).
2
The aggregate regulatory capital measure for I (non-modellable idiosyncratic 
credit spread risk factors that have been demonstrated to be appropriate to 
aggregate with zero correlation), J (non-modellable idiosyncratic equity risk 
factors that have been demonstrated to be appropriate to aggregate with zero 
correlation) and the remaining K (risk factors in model-eligible trading desks that 
are non-modellable (SES)) is calculated as follows, where:

### MAR33.17 .94 defines the vega correlation between risk factors k and l as
33.17

(1)
ISES
 is the stress scenario capital requirement for idiosyncratic credit 
NM,i
spread non-modellable risk i from the I risk factors aggregated with zero 
correlation;
(2)
ISES
 is the stress scenario capital requirement for idiosyncratic equity 
NM,j
non-modellable risk j from the J risk factors aggregated with zero 
correlation;
(3)
SES
 is the stress scenario capital requirement for non-modellable risk k 
NM,k
from K risk factors; and
(4)
Rho (
 ) is equal to 0.6.
Calculation of default risk capital requirement
Banks must have a separate internal model to measure the default risk of trading 
book positions. The general criteria in 
 to 
 and the qualitative 
MAR30.1
MAR30.4
standards in 
 to 
 also apply to the default risk model.
MAR30.5
MAR30.16

### MAR33.18 .94 defines the vega correlation between risk factors k and l as
33.18

Default risk is the risk of direct loss due to an obligor’s default as well as the 
potential for indirect losses that may arise from a default event. 
33.19
Default risk must be measured using a value-at-risk (VaR) model. 
33.20
(1)
Banks must use a default simulation model with two types of systematic risk 
factors.
(2)
Default correlations must be based on credit spreads or on listed equity 
prices. Correlations must be based on data covering a period of 10 years that 
includes a period of stress as defined in 
 and based on a one-year 
MAR33.5
liquidity horizon.
(3)
Banks must have clear policies and procedures that describe the correlation 
calibration process, documenting in particular in which cases credit spreads 
or equity prices are used.
(4)
Banks have the discretion to apply a minimum liquidity horizon of 60 days to 
the determination of default risk capital (DRC) requirement for equity sub-
portfolios.
(5)
The VaR calculation must be conducted weekly and be based on a one-year 
time horizon at a one-tail, 99.9 percentile confidence level.
FAQ
and 
 state that correlations must be measured 
MAR33.20
MAR33.28
over a liquidity horizon of one year in line with 
, which states 
MAR33.23
that a bank must assume constant positions over the one-year capital 
horizon. However, according to 
, a minimum liquidity 
MAR33.23
horizon of 60 days can be applied to equity sub-portfolios. Should the 
correlations for equity sub-portfolios be calibrated utilising a 60-day 
liquidity horizon for consistency?
Banks are permitted to calibrate correlations to liquidity horizons of 60 
days in the case that a separate calculation is performed for equity sub-
portfolios and these desks deal predominately in equity exposures. In 
the case of a desk with both equity and bond exposures, for which a 
joint calculation for default risk of equities and bonds needs to be 
performed, the correlations need to be calibrated to a liquidity horizon 
of one year.
In this case, a bank is permitted to consistently use a 60-day 
probability of default (PD) for equities and a one-year PD for bonds.
FAQ1
(2) states: “Default correlations must be based on credit 
MAR33.20
spreads or on listed equity prices.” Are banks permitted to also include 
additional data sources (eg rating time series) in addition to equity 
prices in order to correct for a correlation bias observed in equity data?
Only credit spreads or listed equity prices are permitted. No additional 
data sources (eg rating time series) are permitted.
FAQ2
(1) specifies that banks must use a default simulation model 
MAR33.20
with two types of systematic risk factors. To meet this condition, should 
the model always have two random variables that correspond to the 
systematic risk factors?
Yes. Systematic risk in a DRC requirement model must be accounted 
for via multiple systematic factors of two different types. The random 
variable that determines whether an obligor defaults must be an 
obligor-specific function of the systematic factors of both types and of
an idiosyncratic factor. For example, in a Merton-type model, obligor
defaults when its asset return
falls below an obligor-specific
threshold that determines the obligor’s probability of default. 
Systematic risk can be described via
systematic regional factors
(
) and
systematic industry factors
(
FAQ3
). For each obligor
, region factor loadings
and
industry factor loadings
that describe the sensitivity of the
obligor’s asset return to each systematic factor need to be chosen. 
There must be at least one non-zero factor loading for the region type 
and at least one non-zero factor loading for the industry type. The
asset return of obligor
can be represented as
, where
is the
idiosyncratic risk factor and
is the idiosyncratic factor loading.
Is a 60-day liquidity horizon permitted to be used for all equity 
positions? Are banks permitted to use a longer liquidity horizon where 
appropriate, eg where equity is held to hedge hybrid positions (such as 
convertibles)?
Yes, banks are permitted to use a 60-day liquidity horizon for all equity 
positions but are permitted to use a longer liquidity horizon where 
appropriate.
FAQ4
All positions subject to market risk capital requirements that have default risk as 
defined in 
, with the exception of those positions subject to the 
MAR33.19
standardised approach, are subject to the DRC requirement model.

### MAR33.21 .94 defines the vega correlation between risk factors k and l as
33.21

(1)
Sovereign exposures (including those denominated in the sovereign’s 
domestic currency), equity positions and defaulted debt positions must be 
included in the model.
(2)
For equity positions, the default of an issuer must be modelled as resulting 
in the equity price dropping to zero.
The DRC requirement model capital requirement is the greater of: 
33.22
(1)
the average of the DRC requirement model measures over the previous 12 
weeks; or
(2)
the most recent DRC requirement model measure.
A bank must assume constant positions over the one-year horizon, or 60 days in 
the context of designated equity sub-portfolios. 
33.23
FAQ
and 
 state that correlations must be measured 
MAR33.20
MAR33.27
over a liquidity horizon of one year in line with 
, which states 
MAR33.23
that a bank must assume constant positions over the one-year capital 
horizon. However, according to 
, a minimum liquidity 
MAR33.23
horizon of 60 days can be applied to equity sub-portfolios. Should the 
correlations for equity sub-portfolios be calibrated utilising a 60-day 
liquidity horizon for consistency?
Banks are permitted to calibrate correlations to liquidity horizons of 60 
days in the case that a separate calculation is performed for equity sub-
portfolios and these desks deal predominately in equity exposures. In 
the case of a desk with both equity and bond exposures, for which a 
joint calculation for default risk of equities and bonds needs to be 
performed, the correlations need to be calibrated to a liquidity horizon 
of one year.
In this case, a bank is permitted to consistently use a 60-day 
probability of default (PD) for equities and a one-year PD for bonds.
FAQ1
states that a bank must have constant positions over the 
MAR33.23
chosen liquidity horizon. However, 
 states that a bank must 
MAR33.28
capture material mismatches between the position and its hedge. 
Please explain how these two paragraphs are to be consistently applied 
to securities with a maturity of less than one year.
The concept of constant positions has changed in the market risk 
framework because the capital horizon is now meant to always be 
synonymous with the new definition of liquidity horizon and no new 
positions are added when positions expire during the capital horizon. 
For securities with a maturity under one year, a constant position can 
be maintained within the liquidity horizon but, much like under the 
Basel II.5 incremental risk charge, any maturity of a long or short 
position must be accounted for when the ability to maintain a constant 
position within the liquidity horizon cannot be contractually assured.
FAQ2
Default risk must be measured for each obligor.
33.24
(1)
Probabilities of default (PDs) implied from market prices are not acceptable 
unless they are corrected to obtain an objective probability of default.3
(2)
PDs are subject to a floor of 0.03%.
Footnotes
Market-implied PDs are not acceptable.
3
A bank’s model may reflect netting of long and short exposures to the same 
obligor. If such exposures span different instruments with exposure to the same 
obligor, the effect of the netting must account for different losses in the different 
instruments (eg differences in seniority).

### MAR33.25 .94 defines the vega correlation between risk factors k and l as
33.25

The basis risk between long and short exposures of different obligors must be 
modelled explicitly. The potential for offsetting default risk among long and short 
exposures across different obligors must be included through the modelling of 
defaults. The pre-netting of positions before input into the model other than as 
described in 
 is not allowed.
MAR33.25

### MAR33.26 .94 defines the vega correlation between risk factors k and l as
33.26

The DRC requirement model must recognise the impact of correlations between 
defaults among obligors, including the effect on correlations of periods of stress 
as described below.

### MAR33.27 .94 defines the vega correlation between risk factors k and l as
33.27

(1)
These correlations must be based on objective data and not chosen in an 
opportunistic way where a higher correlation is used for portfolios with a mix 
of long and short positions and a low correlation used for portfolios with 
long only exposures.
(2)
A bank must validate that its modelling approach for these correlations is 
appropriate for its portfolio, including the choice and weights of its 
systematic risk factors. A bank must document its modelling approach and 
the period of time used to calibrate the model.
(3)
These correlations must be measured over a liquidity horizon of one year.
(4)
These correlations must be calibrated over a period of at least 10 years.
(5)
Banks must reflect all significant basis risks in recognising these correlations, 
including, for example, maturity mismatches, internal or external ratings, 
vintage etc.
FAQ
and 
 state that correlations must be measured 
MAR33.20
MAR33.27
over a liquidity horizon of one year in line with 
, which states 
MAR33.23
that a bank must assume constant positions over the one-year capital 
horizon. However, according to 
, a minimum liquidity 
MAR33.23
horizon of 60 days can be applied to equity sub-portfolios. Should the 
correlations for equity sub-portfolios be calibrated utilising a 60-day 
liquidity horizon for consistency?
Banks are permitted to calibrate correlations to liquidity horizons of 60 
days in the case that a separate calculation is performed for equity sub-
portfolios and these desks deal predominately in equity exposures. In 
the case of a desk with both equity and bond exposures, for which a 
joint calculation for default risk of equities and bonds needs to be 
performed, the correlations need to be calibrated to a liquidity horizon 
of one year.
In this case, a bank is permitted to consistently use a 60-day PD for 
equities and a one-year PD for bonds.
FAQ1
states that a bank must have constant positions over the 
MAR33.23
chosen liquidity horizon. However, 
 states that a bank must 
MAR33.28
capture material mismatches between the position and its hedge. 
Please explain how these two paragraphs are to be consistently applied 
to securities with a maturity of less than one year.
The concept of constant positions has changed in the market risk 
framework because the capital horizon is now meant to always be 
synonymous with the new definition of liquidity horizon and no new 
positions are added when positions expire during the capital horizon. 
For securities with a maturity under one year, a constant position can 
be maintained within the liquidity horizon but, much like under the 
Basel II.5 incremental risk charge, any maturity of a long or short 
position must be accounted for when the ability to maintain a constant 
position within the liquidity horizon cannot be contractually assured.
FAQ2
The bank’s model must capture any material mismatch between a position and its 
hedge. With respect to default risk within the one-year capital horizon, the model 
must account for the risk in the timing of defaults to capture the relative risk from 
the maturity mismatch of long and short positions of less than one-year maturity.

### MAR33.28 .94 defines the vega correlation between risk factors k and l as
33.28

The bank’s model must reflect the effect of issuer and market concentrations, as 
well as concentrations that can arise within and across product classes during 
stressed conditions.

### MAR33.29 .94 defines the vega correlation between risk factors k and l as
33.29

As part of this DRC requirement model, the bank must calculate, for each and 
every position subjected to the model, an incremental loss amount relative to the 
current valuation that the bank would incur in the event that the obligor of the 
position defaults.

### MAR33.30 .94 defines the vega correlation between risk factors k and l as
33.30

Loss estimates must reflect the economic cycle; for example, the model must 
incorporate the dependence of the recovery on the systemic risk factors. 
33.31
The bank’s model must reflect the non-linear impact of options and other 
positions with material non-linear behaviour with respect to default. In the case 
of equity derivatives positions with multiple underlyings, simplified modelling 
approaches (for example modelling approaches that rely solely on individual 
jump-to-default sensitivities to estimate losses when multiple underlyings 
default) may be applied (subject to supervisory approval).

### MAR33.32 .94 defines the vega correlation between risk factors k and l as
33.32

FAQ
indicates that a bank may use a simplified modelling 
MAR33.32
approach for equity derivative positions with multiple underlyings. May 
a similar simplified approach be used for non-correlation trading 
portfolio credit derivative positions with multiple underlyings?
No. The simplified treatment applies only to equity derivatives.
FAQ1
Default risk must be assessed from the perspective of the incremental loss from 
default in excess of the mark-to-market losses already taken into account in the 
current valuation.

### MAR33.33 .94 defines the vega correlation between risk factors k and l as
33.33

Owing to the high confidence standard and long capital horizon of the DRC 
requirement, robust direct validation of the DRC model through standard 
backtesting methods at the 99.9%/one-year soundness standard will not be 
possible.

### MAR33.34 .94 defines the vega correlation between risk factors k and l as
33.34

(1)
Accordingly, validation of a DRC model necessarily must rely more heavily on 
indirect methods including but not limited to stress tests, sensitivity analyses 
and scenario analyses, to assess its qualitative and quantitative 
reasonableness, particularly with regard to the model’s treatment of 
concentrations.
(2)
Given the nature of the DRC soundness standard, such tests must not be 
limited to the range of events experienced historically.
(3)
The validation of a DRC model represents an ongoing process in which 
supervisors and firms jointly determine the exact set of validation procedures 
to be employed.
Banks should strive to develop relevant internal modelling benchmarks to assess 
the overall accuracy of their DRC models.
33.35
Due to the unique relationship between credit spread and default risk, banks 
must seek approval for each trading desk with exposure to these risks, both for 
credit spread risk and default risk. Trading desks which do not receive approval 
will be deemed ineligible for internal modelling standards and be subject to the 
standardised capital framework.

### MAR33.36 .94 defines the vega correlation between risk factors k and l as
33.36

Where a bank has approved PD estimates as part of the internal ratings-based 
(IRB) approach, this data must be used. Where such estimates do not exist, or the 
bank’s supervisor determines that they are not sufficiently robust, PDs must be 
computed using a methodology consistent with the IRB methodology and satisfy 
the following conditions.

### MAR33.37 .94 defines the vega correlation between risk factors k and l as
33.37

(1)
Risk-neutral PDs should not be used as estimates of observed (historical) 
PDs.
(2)
PDs must be measured based on historical default data including both 
formal default events and price declines equivalent to default losses. Where 
possible, this data should be based on publicly traded securities over a 
complete economic cycle. The minimum historical observation period for 
calibration purposes is five years.
(3)
PDs must be estimated based on historical data of default frequency over a 
one-year period. The PD may also be calculated on a theoretical basis (eg 
geometric scaling) provided that the bank is able to demonstrate that such 
theoretical derivations are in line with historical default experience.
(4)
PDs provided by external sources may also be used by banks, provided they 
can be shown to be relevant for the bank’s portfolio.
Where a bank has approved loss-given-default (LGD)4 estimates as part of the IRB 
approach, this data must be used. Where such estimates do not exist, or the 
supervisor determines that they are not sufficiently robust, LGDs must be 
computed using a methodology consistent with the IRB methodology and satisfy 
the following conditions.

### MAR33.38 .94 defines the vega correlation between risk factors k and l as
33.38

Footnotes
Calculation of capital requirement for model-ineligible trading desks
Aggregation of capital requirement
(1)
LGDs must be determined from a market perspective, based on a position’s 
current market value less the position’s expected market value subsequent 
to default. The LGD should reflect the type and seniority of the position and 
cannot be less than zero.
(2)
LGDs must be based on an amount of historical data that is sufficient to 
derive robust, accurate estimates.
(3)
LGDs provided by external sources may also be used by institutions, 
provided they can be shown to be relevant for the bank’s portfolio.
LGD should be interpreted in this context as 1 – recovery rate.
4
Banks must establish a hierarchy ranking their preferred sources for PDs and 
LGDs, in order to avoid the cherry-picking of parameters.
33.39
The regulatory capital requirement associated with trading desks that are either 
out-of-scope for model approval or that have been deemed ineligible to use an 
internal model (Cu) is to be calculated by aggregating all such risks and applying 
the standardised approach.

### MAR33.40 .94 defines the vega correlation between risk factors k and l as
33.40

The aggregate (non-DRC) capital requirement for those trading desks approved 
and eligible for the IMA (ie trading desks that pass the backtesting requirements 
and that have been assigned to the PLA test green zone or amber zone (C ) in 
A
 to 
) is equal to the maximum of the most recent observation 
MAR32.43
MAR32.45
and a weighted average of the previous 60 days scaled by a multiplier and is 
calculated as follows where SES is the aggregate regulatory capital measure for 
the risk factors in model-eligible trading desks that are non-modellable.

### MAR33.41 .94 defines the vega correlation between risk factors k and l as
33.41

The multiplication factor m is fixed at 1.5 unless it is set at a higher level by the 
c
supervisory authority to reflect the addition of a qualitative add on and/or a 
backtesting add-on per the following considerations.

### MAR33.42 .94 defines the vega correlation between risk factors k and l as
33.42

(1)
Banks must add to this factor a “plus” directly related to the ex-post 
performance of the model, thereby introducing a built-in positive incentive 
to maintain the predictive quality of the model.
(2)
For the backtesting add-on, the plus will range from 0 to 0.5 based on the 
outcome of the backtesting of the bank’s daily VaR at the 99th percentile 
based on current observations on the full set of risk factors (VaR
). 
FC
(3)
If the backtesting results are satisfactory and the bank meets all of the 
qualitative standards set out in 
 to 
, the plus factor could 
MAR30.5
MAR30.16
be zero. 
 presents in detail the approach to be applied for backtesting 
MAR32
and the plus factor.
(4)
The backtesting add-on factor is determined based on the maximum of the 
exceptions generated by the backtesting results against actual P&L (APL) and 
hypothetical P&L (HPL) as described 
.
MAR32
The aggregate capital requirement for market risk (ACR
) is equal to the 
total
aggregate capital requirement for approved and eligible trading desks (IMA
 =C
G,A
+ DRC) plus the standardised approach capital requirement for trading desks 
A 
that are either out-of-scope for model approval or that have been deemed 
ineligible to use the internal models approach (C ). If at least one eligible trading 
U
desk is in the PLA test amber zone, a capital surcharge is added. The impact of 
the capital surcharge is limited by the formula:

### MAR33.43 .94 defines the vega correlation between risk factors k and l as
33.43

For the purposes of calculating the capital requirement, the risk factor eligibility 
test, the PLA test and the trading desk-level backtesting are applied on a 
quarterly basis to update the modellability of risk factors and desk classification 
to the PLA test green zone, amber zone, or red zone. In addition, the stressed 
period and the reduced set of risk factors (E
 and E
) must be updated on a 
R,C
R,S
quarterly basis. The reference dates to perform the tests and to update the stress 
period and selection of the reduced set of risk factors should be consistent. Banks 
must reflect updates to the stressed period and to the reduced set of risk factors 
as well as the test results in calculating capital requirements in a timely manner. 
The averages of the previous 60 days (IMCC, SES) and or respectively 12 weeks 
(DRC) have only to be calculated at the end of the quarter for the purpose of 
calculating the capital requirement.

### MAR33.44 .94 defines the vega correlation between risk factors k and l as
33.44

The capital surcharge is calculated as the difference between the aggregated 
standardised capital charges (SA
) and the aggregated internal models-based 
G,A
capital charges (
 ) multiplied by a factor k. To determine the
aggregated capital charges, positions in all of the trading desks in the PLA green 
zone or amber zone are taken into account. The capital surcharge is floored at 
zero. In the formula below:

### MAR33.45 .94 defines the vega correlation between risk factors k and l as
33.45

(1)
 ;
(2)
 denotes the standardised capital requirement for all the positions of
trading desk “i”;
(3)
 denotes the indices of all the approved trading desks in the amber 
zone; and
(4)
 denotes the indices of all the approved trading desks in the green 
zone or amber zone.
The risk-weighted assets for market risk under the IMA are determined by 
multiplying the capital requirements calculated as set out in this chapter by 12.5.
33.46

## MAR40 .94 defines the vega correlation between risk factors k and l as

Simplified standardised 
approach
This chapter sets out a simplified standardised 
approach for calculating risk-weighted assets for 
market risk.
Version effective as of
01 Jan 2023
Updated to take account of the revised 
implementation date announced on 27 March 
2020. Cross references to the securitisation 
chapters updated to include a reference to the 
chapter on NPL securitisations (CRE45) published 
on 26 November 2020. Updated to incorporate 
the FAQ published on 5 July 2024.
Risk-weighted assets and capital requirements
The risk-weighted assets for market risk under the simplified standardised 
approach are determined by multiplying the capital requirements calculated as 
set out in this chapter by 12.5.

### MAR40.1 .94 defines the vega correlation between risk factors k and l as
40.1

(1)
 to 
 deal with interest rate, equity, foreign exchange (FX) 
MAR40.3
MAR40.73
and commodities risk.
(2)
 to 
 set out a number of possible methods for 
MAR40.74
MAR40.86
measuring the price risk in options of all kinds.
(3)
The capital requirement under the simplified standardised approach will be 
the measures of risk obtained from 
 to 
, summed 
MAR40.2
MAR40.86
arithmetically.
The capital requirement arising from the simplified standardised approach is the 
simple sum of the recalibrated capital requirements arising from each of the four 
risk classes – namely interest rate risk, equity risk, FX risk and commodity risk as 
detailed in the formula below, where:

### MAR40.2 .94 defines the vega correlation between risk factors k and l as
40.2

(1)
 = capital requirement under 
 to 
 (interest rate risk), 
MAR40.3
MAR40.40
plus additional requirements for option risks from debt instruments (non-
delta risks) under 
 to 
 (treatment of options);
MAR40.74
MAR40.86
(2)
 = capital requirement under 
 to 
 (equity risk), plus 
MAR40.41
MAR40.52
additional requirements for option risks from equity instruments (non-delta 
risks) under 
 to 
 (treatment of options);
MAR40.74
MAR40.86
(3)
 = capital requirement under 
 to 
 (FX risk), plus 
MAR40.53
MAR40.62
additional requirements for option risks from foreign exchange instruments 
(non-delta risks) under 
 to 
 (treatment of options);
MAR40.74
MAR40.86
(4)
 = capital requirement under 
 to 
 (commodities 
MAR40.63
MAR40.73
risk), plus additional requirements for option risks from commodities 
instruments (non-delta risks) under 
 to 
 (treatment of 
MAR40.74
MAR40.86
options);
(5)
 = Scaling factor of 1.30;
Interest rate risk
Footnotes
(6)
 = Scaling factor of 3.50;
(7)
 = Scaling factor of 1.90; and
(8)
 = Scaling factor of 1.20.
FAQ
Should the scaling factors under the simplified standardised approach 
be applied to capital requirements calculated for securitisation 
positions?
The scaling factor for interest rate risk should be applied to all capital 
requirements calculated in 
 to 
.
MAR40.3
MAR40.40
FAQ1
This section sets out the simplified standard approach for measuring the risk of 
holding or taking positions in debt securities and other interest rate related 
instruments in the trading book. The instruments covered include all fixed-rate 
and floating-rate debt securities and instruments that behave like them, including 
non-convertible preference shares.1 Convertible bonds, ie debt issues or 
preference shares that are convertible, at a stated price, into common shares of 
the issuer, will be treated as debt securities if they trade like debt securities and 
as equities if they trade like equities. The basis for dealing with derivative 
products is considered in 
 to 
.
MAR40.31
MAR40.40

### MAR40.3 .94 defines the vega correlation between risk factors k and l as
40.3

Traded mortgage securities and mortgage derivative products possess 
unique characteristics because of the risk of prepayment. Accordingly, 
for the time being, no common treatment will apply to these securities, 
which will be dealt with at national discretion. A security that is the 
subject of a repurchase or securities lending agreement will be treated 
as if it were still owned by the lender of the security, ie it will be treated 
in the same manner as other securities positions.
1
Specific risk
The minimum capital requirement is expressed in terms of two separately 
calculated amounts, one applying to the “specific risk” of each security, whether it 
is a short or a long position, and the other to the interest rate risk in the portfolio 
(termed “general market risk”) where long and short positions in different 
securities or instruments can be offset.

### MAR40.4 .94 defines the vega correlation between risk factors k and l as
40.4

The capital requirement for specific risk is designed to protect against an adverse 
movement in the price of an individual security owing to factors related to the 
individual issuer. In measuring the risk, offsetting will be restricted to matched 
positions in the identical issue (including positions in derivatives). Even if the 
issuer is the same, no offsetting will be permitted between different issues since 
differences in coupon rates, liquidity, call features, etc mean that prices may 
diverge in the short run.

### MAR40.5 .94 defines the vega correlation between risk factors k and l as
40.5

FAQ
What could be the conditions under which trading book positions that 
are subject to interest rate specific risk could be netted in order to 
derive either the net long position or the net short position? Are the 
rules considering a perfect hedge only? Is it allowed to net cash and 
synthetic securitisations for the purpose of the capital calculation for 
structured products under the simplified standardised approach for 
correlation trading?
Netting is only allowed under limited circumstances for interest rate 
specific risk as explained in 
: “offsetting will be restricted to 
MAR40.5
matched positions in the identical issue (including positions in 
derivatives). Even if the issuer is the same, no offsetting will be 
permitted between different issues since differences in coupon rates, 
liquidity, call features, etc means that prices may diverge in the short 
run.”
In addition, partial offsetting is allowed in two other sets of 
circumstances. One set of circumstances is described in 
 and 
MAR40.21
concerns nth-to-default basked products. The other set of 
circumstances described in 
 to 
 pertains to 
MAR40.16
MAR40.18
offsetting between a credit derivative (whether total return swap or 
credit default swap) and the underlying exposure (ie cash position). 
Although this treatment applies generally in a one-for-one fashion, it is 
possible that multiple instruments could combine to create a hedge 
that would be eligible for consideration for partial offsetting. 
Supervisors should recognise that, in the case of multiple instruments 
comprising one side of the position, necessary conditions (ie the value 
of two legs moving in opposite directions, key contractual features of 
the credit derivative, identical reference obligations and currency
/maturity mismatches) will be extremely difficult to meet, in practice.
FAQ1
The specific risk capital requirements for “government” and “other” categories will 
be as follows:
40.6
Specific risk capital requirements for issuer risk
Government and “other” categories
Table 1
Categories
External credit
assessment
Specific risk capital requirement
Government
AAA to AA–
0%
A+ to BBB–
0.25% (residual term to final maturity 6 months or 
less)
1.00% (residual term to final maturity greater than 6 
and up to and including 24 months)
1.60% (residual term to final maturity exceeding 24 
months)
BB+ to B–
8.00%
Below B–
12.00%
Unrated
8.00%
Qualifying
0.25% (residual term to final maturity 6 months or 
less)
1.00% (residual term to final maturity greater than 6 
and up to and including 24 months)
1.60% (residual term to final maturity exceeding 24 
months)
Other 
BB+ to BB–
8.00%
Below BB–
12.00%
Unrated
8.00%
The government category will include all forms of government2 paper including 
bonds, treasury bills and other short-term instruments, but national authorities 
reserve the right to apply a specific risk capital requirement to securities issued 
by certain foreign governments, especially to securities denominated in a 
currency other than that of the issuing government.

### MAR40.7 .94 defines the vega correlation between risk factors k and l as
40.7

Footnotes
Footnotes
Including, at national discretion, local and regional governments 
subject to a zero credit risk weight in 
.
CRE20
2
When the government paper is denominated in the domestic currency and 
funded by the bank in the same currency, at national discretion a lower specific 
risk capital requirement may be applied.

### MAR40.8 .94 defines the vega correlation between risk factors k and l as
40.8

The qualifying category includes securities issued by public sector entities and 
multilateral development banks, plus other securities that are:
40.9
(1)
rated investment grade (IG)3 by at least two credit rating agencies specified 
by the national authority; or
(2)
rated IG by one rating agency and not less than IG by any other rating 
agency specified by the national authority (subject to supervisory oversight); 
or
(3)
subject to supervisory approval, unrated, but deemed to be of comparable 
investment quality by the reporting bank, and the issuer has securities listed 
on a recognised stock exchange.
For example, IG include rated Baa or higher by Moody’s and BBB or 
higher by Standard and Poor’s.
3
Each supervisory authority will be responsible for monitoring the application of 
these qualifying criteria, particularly in relation to the last criterion where the 
initial classification is essentially left to the reporting banks. National authorities 
will also have discretion to include within the qualifying category debt securities 
issued by banks in countries which have implemented this framework, subject to 
the express understanding that supervisory authorities in such countries 
undertake prompt remedial action if a bank fails to meet the capital standards set 
forth in this framework. Similarly, national authorities will have discretion to 
include within the qualifying category debt securities issued by securities firms 
that are subject to equivalent rules.

### MAR40.10 .94 defines the vega correlation between risk factors k and l as
40.10

Furthermore, the qualifying category shall include securities issued by institutions 
that are deemed to be equivalent to IG quality and subject to supervisory and 
regulatory arrangements comparable to those under this framework.

### MAR40.11 .94 defines the vega correlation between risk factors k and l as
40.11

Footnotes
Unrated securities may be included in the qualifying category when they are 
subject to supervisory approval, unrated, but deemed to be of comparable
investment quality by the reporting bank, and the issuer has securities listed on a 
recognised stock exchange. This will remain unchanged for banks using the 
simplified standardised approach. For banks using the internal ratings-based (IRB) 
approach for a portfolio, unrated securities can be included in the qualifying 
category if both of the following conditions are met:

### MAR40.12 .94 defines the vega correlation between risk factors k and l as
40.12

(1)
the securities are rated equivalent4 to IG under the reporting bank’s internal 
rating system, which the national supervisor has confirmed complies with the 
requirements for an IRB approach; and
(2)
the issuer has securities listed on a recognised stock exchange.
Equivalent means the debt security has a one-year probability of 
default (PD) equal to or less than the one year PD implied by the long-
run average one-year PD of a security rated IG or better by a 
qualifying rating agency.
4
However, since this may in certain cases considerably underestimate the specific 
risk for debt instruments which have a high yield to redemption relative to 
government debt securities, each national supervisor will have the discretion:

### MAR40.13 .94 defines the vega correlation between risk factors k and l as
40.13

(1)
to apply a higher specific risk charge to such instruments; and/or
(2)
to disallow offsetting for the purposes of defining the extent of general 
market risk between such instruments and any other debt instruments.
The specific risk capital requirement of securitisation positions as defined in
to 
 that are held in the trading book is to be calculated 
CRE40.1
CRE40.6
according to the revised method for such positions in the banking book as set 
out in 
 to 
CRE40
CRE45. A bank shall calculate the specific risk capital requirement 
applicable to each net securitisation position by dividing the risk weight 
calculated as if it were held in the banking book by 12.5.

### MAR40.14 .94 defines the vega correlation between risk factors k and l as
40.14

Banks may limit the capital requirement for an individual position in a credit 
derivative or securitisation instrument to the maximum possible loss. For a short 
risk position this limit could be calculated as a change in value due to the 
underlying names immediately becoming default risk-free. For a long risk 
position, the maximum possible loss could be calculated as the change in value in 
the event that all the underlying names were to default with zero recoveries. The 
maximum possible loss must be calculated for each individual position.

### MAR40.15 .94 defines the vega correlation between risk factors k and l as
40.15

FAQ
When a bank buys credit protection for an asset-backed security (ABS) 
tranche and (due to netting rules) the bank is treated as having a net 
short position, the simplified standardised capital requirement for the 
net short position is often determined by the max potential loss. This is 
particularly true when the underlying ABS tranche has been severely 
downgraded and written down. In particular, banks note that if the 
underlying ABS continues to deteriorate, the overall capital 
requirement progressively increases and is dominated by the charge 
against the short side of the hedged position.
Some examples (without and with off-set) illustrate how the Max Loss 
principle should apply.
Max loss without offset:
Suppose the bank has net long and net short positions that reference 
similar, but not the same, underlying assets. In other words the bank 
hedges an A-rated mezzanine residential mortgage-backed security 
(RMBS) tranche (notional = USD 100) with a credit default swap (CDS) 
on a similar but different A-rated mezzanine RMBS (also having 
notional = USD 100).
Suppose the RMBS tranche owned by the bank is now rated C, and has 
value of USD 15. Also assume that the value of the CDS on the 
different RMBS has a current value of USD 80. Further, suppose that 
the current value of the RMBS underlying this CDS is USD 20 and is 
also rated C. Finally, suppose that the CDS would be valued at USD –2 
if the underlying RMBS tranche were to recover unexpectedly and 
become risk-free.
The correct treatment is as follows: min (USD 15, USD 15) (long leg) + 
min (USD 20, USD 82) (short leg) = USD 35.
No off-set would be permissible in this example, because the same 
underlying asset has not been hedged. The capital requirement should, 
therefore, be calculated by summing the charges against the long and 
short legs. The maximum loss principle would apply to each individual 
position.
Please note that the market value of the underlying has been applied 
in determining the exposure value of the CDS.
Max loss with offset:
FAQ1
Footnotes
Suppose the bank hedges an A-rated mezzanine RMBS tranche with a 
CDS referencing the same RMBS having notional of USD 100. Suppose 
the RMBS tranche is now rated C, and has value USD 15, while the 
current value of the CDS is USD 85. Suppose that the value of the CDS 
would equal USD –2 if the RMBS tranche were to recover unexpectedly 
and become risk-free.
In this example, if the CDS exactly matched the RMBS in tenor, then 
offsetting could potentially apply. In that instance, the capital 
requirement should equal 20% of max{min(USD 15, USD 15), min(USD 
15, USD 87)} = USD 3.
If the tenors were not matched (ie maturity mismatch), then the capital 
requirement should equal max{min(USD 15, USD 15), min(USD 15, 
USD 87)} = USD 15.
Please note that the maximum loss principle cannot be applied on a 
portfolio basis.
Full allowance will be recognised for positions hedged by credit derivatives when 
the values of two legs (ie long and short) always move in the opposite direction 
and broadly to the same extent. This would be the case in the following 
situations, in which cases no specific risk capital requirement applies to both sides 
of the position:

### MAR40.16 .94 defines the vega correlation between risk factors k and l as
40.16

(1)
the two legs consist of completely identical instruments; or
(2)
a long cash position (or credit derivative) is hedged by a total rate of return 
swap (or vice versa) and there is an exact match between the reference 
obligation and the underlying exposure (ie the cash position).5
The maturity of the swap itself may be different from that of the 
underlying exposure.
5
FAQ
According to 
 to 
, the offsetting treatment is 
MAR40.16
MAR40.18
applied to a cash position that is hedged by a credit derivative or a 
credit derivative that is hedged by another credit derivative, assuming 
there is an exact match in terms of the reference obligations. Please 
illustrate the treatment.
to 
, are applicable not only when the underlying 
MAR40.16
MAR40.18
position being hedged is a cash position, but also when the position 
being hedged is a credit default swap (CDS) or other credit derivative. 
They also apply regardless of whether the cash positions or reference 
obligations of the credit derivative are single-name or securitisation 
exposures.
For example, when a long cash position is hedged using a CDS, the 
80% offset treatment of 
 (the partial allowance treatment of 
MAR40.17
) generally applies when the reference obligation of the CDS 
MAR40.18
is the cash instrument being hedged and the currencies and remaining 
maturities of the two positions are (are not) identical. Similarly, when a 
purchased CDS is hedged with a sold CDS, the 80% offset treatment 
(the partial allowance treatment) generally applies when both the long 
and short CDSs have the same reference obligations and the currencies 
and remaining maturities of the long and short CDSs are (are not) 
identical. The full allowance (100% offset) treatment generally applies 
only when there is zero basis risk between the instrument being 
hedged and the hedging instrument, such as when a cash position is 
hedged with a total rate of return swap referencing the same cash 
instrument and there is no currency mismatch, or when a purchased 
CDS position is hedged by selling a CDS with identical terms in all 
respects, including reference obligation, currency, maturity, 
documentation clauses (eg credit payout events, methods for 
determining payouts for credit events, etc), and structure of fixed and 
variable payments over time.
As explained in FAQ1 to 
, it is worth noting that the conditions 
MAR40.5
under which partial or full offsetting of risk positions that are subject to 
interest rate specific risk are narrowly defined. In practice, offsets 
between securitisation positions and credit derivatives are unlikely to 
be recognised in most cases due to the explicit requirements in MAR40.
to 
 on reference names etc.
16
MAR40.18
FAQ1
An 80% offset will be recognised when the value of two legs (ie long and short) 
always moves in the opposite direction but not broadly to the same extent. This 
would be the case when a long cash position (or credit derivative) is hedged by a
credit default swap (CDS) or a credit-linked note (or vice versa) and there is an 
exact match in terms of the reference obligation, the maturity of both the 
reference obligation and the credit derivative, and the currency of the underlying 
exposure. In addition, key features of the credit derivative contract (eg credit 
event definitions, settlement mechanisms) should not cause the price movement 
of the credit derivative to materially deviate from the price movements of the 
cash position. To the extent that the transaction transfers risk (ie taking account 
of restrictive payout provisions such as fixed payouts and materiality thresholds), 
an 80% specific risk offset will be applied to the side of the transaction with the 
higher capital requirement, while the specific risk requirement on the other side 
will be zero.

### MAR40.17 .94 defines the vega correlation between risk factors k and l as
40.17

FAQ
According to 
 to 
, the offsetting treatment is 
MAR40.16
MAR40.18
applied to a cash position that is hedged by a credit derivative or a 
credit derivative that is hedged by another credit derivative, assuming 
there is an exact match in terms of the reference obligations. Please 
illustrate the treatment.
to 
 are applicable not only when the underlying 
MAR40.16
MAR40.18
position being hedged is a cash position, but also when the position 
being hedged is a CDS or other credit derivative. They also apply 
regardless of whether the cash positions or reference obligations of the 
credit derivative are single-name or securitisation exposures.
For example, when a long cash position is hedged using a CDS, the 
80% offset treatment of 
 (the partial allowance treatment of 
MAR40.17
) generally applies when the reference obligation of the CDS 
MAR40.18
is the cash instrument being hedged and the currencies and remaining 
maturities of the two positions are (are not) identical. Similarly, when a 
purchased CDS is hedged with a sold CDS, the 80% offset treatment 
(the partial allowance treatment) generally applies when both the long 
and short CDSs have the same reference obligations and the currencies 
and remaining maturities of the long and short CDSs are (are not) 
identical. The full allowance (100% offset) treatment generally applies 
only when there is zero basis risk between the instrument being 
hedged and the hedging instrument, such as when a cash position is 
hedged with a total rate of return swap referencing the same cash 
instrument and there is no currency mismatch, or when a purchased 
CDS position is hedged by selling a CDS with identical terms in all 
respects, including reference obligation, currency, maturity, 
documentation clauses (eg credit payout events, methods for 
determining payouts for credit events, etc), and structure of fixed and 
variable payments over time.
As explained in FAQ1 to 
, it is worth noting that the conditions 
MAR40.5
under which partial or full offsetting of risk positions that are subject to 
interest rate specific risk are narrowly defined. In practice, offsets 
between securitisation positions and credit derivatives are unlikely to 
be recognised in most cases due to the explicit requirements in MAR40.
to 
 on reference names etc.
16
MAR40.18
FAQ1
Partial allowance will be recognised when the value of the two legs (ie long and 
short) usually moves in the opposite direction. This would be the case in the 
following situations:

### MAR40.18 .94 defines the vega correlation between risk factors k and l as
40.18

Footnotes
(1)
The position is captured in 
(2), but there is an asset mismatch 
MAR40.16
between the reference obligation and the underlying exposure. Nonetheless, 
the position meets the requirements in 
.
CRE22.74
(2)
The position is captured in 
(1) or 
 but there is a currency 
MAR40.16
MAR40.17
or maturity mismatch6 between the credit protection and the underlying 
asset.
(3)
The position is captured in 
 but there is an asset mismatch 
MAR40.17
between the cash position (or credit derivative) and the credit derivative 
hedge. However, the underlying asset is included in the (deliverable) 
obligations in the credit derivative documentation.
Currency mismatches should feed into the normal reporting of FX risk.
6
FAQ
According to 
 to 
, the offsetting treatment is 
MAR40.16
MAR40.18
applied to a cash position that is hedged by a credit derivative or a 
credit derivative that is hedged by another credit derivative, assuming 
there is an exact match in terms of the reference obligations. Please 
illustrate the treatment.
to 
 are applicable not only when the underlying 
MAR40.16
MAR40.18
position being hedged is a cash position, but also when the position 
being hedged is a CDS or other credit derivative. They also apply 
regardless of whether the cash positions or reference obligations of the 
credit derivative are single-name or securitisation exposures.
For example, when a long cash position is hedged using a CDS, the 
80% offset treatment of 
 (the partial allowance treatment of 
MAR40.17
) generally applies when the reference obligation of the CDS 
MAR40.18
is the cash instrument being hedged and the currencies and remaining 
maturities of the two positions are (are not) identical. Similarly, when a 
purchased CDS is hedged with a sold CDS, the 80% offset treatment 
(the partial allowance treatment) generally applies when both the long 
and short CDSs have the same reference obligations and the currencies 
and remaining maturities of the long and short CDSs are (are not) 
identical. The full allowance (100% offset) treatment generally applies 
only when there is zero basis risk between the instrument being 
hedged and the hedging instrument, such as when a cash position is 
hedged with a total rate of return swap referencing the same cash 
instrument and there is no currency mismatch, or when a purchased 
CDS position is hedged by selling a CDS with identical terms in all 
respects, including reference obligation, currency, maturity, 
documentation clauses (eg credit payout events, methods for 
determining payouts for credit events, etc), and structure of fixed and 
variable payments over time.
As explained in FAQ1 to 
, it is worth noting that the conditions 
MAR40.5
under which partial or full offsetting of risk positions that are subject to 
interest rate specific risk are narrowly defined. In practice, offsets 
between securitisation positions and credit derivatives are unlikely to 
be recognised in most cases due to the explicit requirements in MAR40.
to 
 on reference names etc.
16
MAR40.18
FAQ1
In each of these cases in 
 to 
, the following rule applies. 
MAR40.16
MAR40.18
Rather than adding the specific risk capital requirements for each side of the 
transaction (ie the credit protection and the underlying asset) only the higher of 
the two capital requirements will apply.

### MAR40.19 .94 defines the vega correlation between risk factors k and l as
40.19

In cases not captured in 
 to 
, a specific risk capital 
MAR40.16
MAR40.18
requirement will be assessed against both sides of the position.
40.20
An nth-to-default credit derivative is a contract where the payoff is based on the 
nth asset to default in a basket of underlying reference instruments. Once the nth 
default occurs the transaction terminates and is settled.

### MAR40.21 .94 defines the vega correlation between risk factors k and l as
40.21

(1)
The capital requirement for specific risk for a first-to-default credit derivative 
is the lesser of:
(a)
the sum of the specific risk capital requirements for the individual 
reference credit instruments in the basket; and
(b)
the maximum possible credit event payment under the contract.
(2)
Where a bank has a risk position in one of the reference credit instruments 
underlying a first-to-default credit derivative and this credit derivative 
hedges the bank’s risk position, the bank is allowed to reduce, with respect 
to the hedged amount, both the capital requirement for specific risk for the 
reference credit instrument and that part of the capital requirement for 
specific risk for the credit derivative that relates to this particular reference 
credit instrument. Where a bank has multiple risk positions in reference 
credit instruments underlying a first-to-default credit derivative, this offset is 
allowed only for that underlying reference credit instrument having the 
lowest specific risk capital requirement.
(3)
The capital requirement for specific risk for an nth-to-default credit 
derivative with n greater than one is the lesser of:
(a)
the sum of the specific risk capital requirements for the individual 
reference credit instruments in the basket but disregarding the (n-1) 
obligations with the lowest specific risk capital requirements; and
(b)
the maximum possible credit event payment under the contract. For nth-
to-default credit derivatives with n greater than 1, no offset of the 
capital requirement for specific risk with any underlying reference credit 
instrument is allowed.
(4)
If a first or other nth-to-default credit derivative is externally rated, then the 
protection seller must calculate the specific risk capital requirement using 
the rating of the derivative and apply the respective securitisation risk 
weights as specified in 
, as applicable.
MAR40.14
(5)
The capital requirement against each net nth-to-default credit derivative 
position applies irrespective of whether the bank has a long or short 
position, ie obtains or provides protection.
FAQ
The framework mentions only tranches and nth-to-default products 
explicitly, but not nth to n+m-th-to-default products (eg the value 
depends on the default of the 5th, 6th, 7th and 8th default in a pool; 
only in specific cases such as the same nominal for all underlyings can 
this product be represented by, for example, a 5% to 8% tranche). Are 
nth to n+m-th-to-default products covered in the framework?
Yes. Such products are to be decomposed into individual nth-to-default 
products and the rules for nth-to-default products in 
 apply. 
MAR40.21
In the example cited above, the capital requirement for a basket 
default swap covering defaults five to eight would be calculated as the 
sum of the capital requirements for a 5th-to-default swap, a 6th-to-
default swap, a 7th-to-default swap and an 8th-to-default swap.
FAQ1
A bank must determine the specific risk capital requirement for the correlation 
trading portfolio (CTP) as follows: 
40.22
(1)
The bank computes:
(a)
the total specific risk capital requirements that would apply just to the 
net long positions from the net long correlation trading exposures 
combined; and
(b)
the total specific risk capital requirements that would apply just to the 
net short positions from the net short correlation trading exposures 
combined.
(2)
The larger of these total amounts is then the specific risk capital requirement 
for the CTP.
General market risk
FAQ
Can the approach of taking the larger of the specific risk capital 
requirements for net long positions and the specific risk capital 
requirement for net short positions be applied to leveraged 
securitisation positions or option products on securitisation positions?
No. Leveraged securitisation positions and option products on 
securitisation positions are securitisation positions. They are not 
admissible for the CTP. The capital requirements for specific risk will be 
determined as the sum of the capital requirements for specific risk 
against net long and net short positions.
FAQ1
The capital requirements for general market risk are designed to capture the risk 
of loss arising from changes in market interest rates. A choice between two 
principal methods of measuring the risk is permitted – a maturity method and a 
duration method. In each method, the capital requirement is the sum of four 
components:

### MAR40.23 .94 defines the vega correlation between risk factors k and l as
40.23

(1)
the net short or long position in the whole trading book;
(2)
a small proportion of the matched positions in each time band (the “vertical 
disallowance”);
(3)
a larger proportion of the matched positions across different time bands (the 
“horizontal disallowance”); and
(4)
a net charge for positions in options, where appropriate (see 
 and 
MAR40.84
).
MAR40.85
Separate maturity ladders should be used for each currency and capital 
requirements should be calculated for each currency separately and then 
summed with no offsetting between positions of the opposite sign. In the case of 
those currencies in which business is insignificant, separate maturity ladders for 
each currency are not required. Rather, the bank may construct a single maturity 
ladder and slot, within each appropriate time band, the net long or short position 
for each currency. However, these individual net positions are to be summed 
within each time band, irrespective of whether they are long or short positions, to 
produce a gross position figure.

### MAR40.24 .94 defines the vega correlation between risk factors k and l as
40.24

In the maturity method (see 
 for the duration method), long or short 
MAR40.29
positions in debt securities and other sources of interest rate exposures including 
derivative instruments, are slotted into a maturity ladder comprising 13 time
bands (or 15 time bands in the case of low coupon instruments). Fixed rate 
instruments should be allocated according to the residual term to maturity and 
floating-rate instruments according to the residual term to the next repricing 
date. Opposite positions of the same amount in the same issues (but not 
different issues by the same issuer), whether actual or notional, can be omitted 
from the interest rate maturity framework, as well as closely matched swaps, 
forwards, futures and forward rate agreements (FRAs) which meet the conditions 
set out in 
 and 
 below.
MAR40.35
MAR40.36

### MAR40.25 .94 defines the vega correlation between risk factors k and l as
40.25

The first step in the calculation is to weight the positions in each time band by a 
factor designed to reflect the price sensitivity of those positions to assumed 
changes in interest rates. The weights for each time band are set out in Table 4. 
Zero-coupon bonds and deep-discount bonds (defined as bonds with a coupon 
of less than 3%) should be slotted according to the time bands set out in the 
second column of Table 4.

### MAR40.26 .94 defines the vega correlation between risk factors k and l as
40.26

Maturity method: time bands and weights
Table 4
Coupon 3% or more
Coupon less than 3%
Risk weight
Assumed changes in
yield
1 month or less
1 month or less
0.00%
1.00
1 to 3 months
1 to 3 months
0.20%
1.00
3 to 6 months
3 to 6 months
0.40%
1.00
6 to 12 months
6 to 12 months
0.70%
1.00
1 to 2 years
1.0 to 1.9 years
1.25%
0.90
2 to 3 years
1.9 to 2.8 years
1.75%
0.80
3 to 4 years
2.8 to 3.6 years
2.25%
0.75
4 to 5 years
3.6 to 4.3 years
2.75%
0.75
5 to 7 years
4.3 to 5.7 years
3.25%
0.70
7 to 10 years
5.7 to 7.3 years
3.75%
0.65
10 to 15 years
7.3 to 9.3 years
4.50%
0.60
15 to 20 years 
9.3 to 10.6 years
5.25%
0.60
Over 20 years
10.6 to 12 years
6.00%
0.60
12 to 20 years
8.00%
0.60
Over 20 years
12.50%
0.60
The next step in the calculation is to offset the weighted longs and shorts in each 
time band, resulting in a single short or long position for each band. Since, 
however, each band would include different instruments and different maturities, 
a 10% capital requirement to reflect basis risk and gap risk will be levied on the 
smaller of the offsetting positions, be it long or short. Thus, if the sum of the 
weighted longs in a time band is USD 100 million and the sum of the weighted 
shorts USD 90 million, the so-called vertical disallowance for that time band 
would be 10% of USD 90 million (ie USD 9 million).

### MAR40.27 .94 defines the vega correlation between risk factors k and l as
40.27

The result of the above calculations is to produce two sets of weighted positions, 
the net long or short positions in each time band (USD 10 million long in the 
example above) and the vertical disallowances, which have no sign.

### MAR40.28 .94 defines the vega correlation between risk factors k and l as
40.28

(1)
In addition, however, banks will be allowed to conduct two rounds of 
horizontal offsetting:
(a)
first between the net positions in each of three zones, where zone 1 is 
set as zero to one year, zone 2 is set as one year to four years, and zone 
3 is set as four years and over (however, for coupons less than 3%, zone 
2 is set as one year to 3.6 years and zone 3 is set as 3.6 years and over); 
and
(b)
subsequently between the net positions in the three different zones.
Footnotes
(2)
The offsetting will be subject to a scale of disallowances expressed as a 
fraction of the matched positions, as set out in Table 5. The weighted long 
and short positions in each of three zones may be offset, subject to the 
matched portion attracting a disallowance factor that is part of the capital 
requirement. The residual net position in each zone may be carried over and 
offset against opposite positions in other zones, subject to a second set of 
disallowance factors.
Horizontal disallowances
Table 5
Zones7
Time band7
Within the
zone
Between 
adjacent zones
Between zones
1 and 3
0-1 month
Zone 1
1-3 months
40%
3-6 months
6-12 months
40%
1-2 years
Zone 2
2-3 years
30%
100%
3-4 years
4-5 years
40%
5-7 years
Zone 3
7-10 years
10-15 years
30%
15-20 years
Over 20 years
The zones for coupons less than 3% are 0 to 1 year, 1 to 3.6 years, and 
3.6 years and over.
7
Under the alternative duration method, banks with the necessary capability may, 
with their supervisors’ consent, use a more accurate method of measuring all of
their general market risk by calculating the price sensitivity of each position 
separately. Banks must elect and use the method on a continuous basis (unless a 
change in method is approved by the national authority) and will be subject to 
supervisory monitoring of the systems used. The mechanics of this method are as 
follows:

### MAR40.29 .94 defines the vega correlation between risk factors k and l as
40.29

(1)
First calculate the price sensitivity of each instrument in terms of a change in 
interest rates of between 0.6 and 1.0 percentage points depending on the 
maturity of the instrument (see Table 6);
(2)
Slot the resulting sensitivity measures into a duration-based ladder with the 
15 time bands set out in Table 6;
(3)
Subject long and short positions in each time band to a 5% vertical 
disallowance designed to capture basis risk; and
(4)
Carry forward the net positions in each time band for horizontal offsetting 
subject to the disallowances set out in Table 5 above.
Duration method: time bands and assumed changes in yield
Table 6
Assumed change in
yield
Assumed change
in yield
Zone 1: 
Zone 3:
1 month or less
1.00
3.6 to 4.3 years
0.75
1 to 3 months
1.00
4.3 to 5.7 years
0.70
3 to 6 months
1.00
5.7 to 7.3 years
0.65
6 to 12 months
1.00
7.3 to 9.3 years
0.60
Zone 2:
9.3 to 10.6 years
0.60
1.0 to 1.9 years
0.90
10.6 to 12 years
0.60
1.9 to 2.8 years
0.80
12 to 20 years
0.60
2.8 to 3.6 years
0.75
Over 20 years
0.60
Interest rate derivatives
Footnotes
In the case of residual currencies (see 
 above) the gross positions in 
MAR40.24
each time band will be subject to either the risk weightings set out in 
, 
MAR40.26
if positions are reported using the maturity method, or the assumed change in 
yield set out in 
, if positions are reported using the duration method, 
MAR40.29
with no further offsets.

### MAR40.30 .94 defines the vega correlation between risk factors k and l as
40.30

The measurement system should include all interest-rate derivatives and off-
balance sheet instruments in the trading book which react to changes in interest 
rates (eg FRAs, other forward contracts, bond futures, interest rate and cross-
currency swaps and forward foreign exchange positions). Options can be treated 
in a variety of ways as described in 
 to 
. A summary of the 
MAR40.74
MAR40.86
rules for dealing with interest rate derivatives is set out in 
.
MAR40.40

### MAR40.31 .94 defines the vega correlation between risk factors k and l as
40.31

The derivatives should be converted into positions in the relevant underlying and 
become subject to specific and general market risk charges as described above. 
In order to calculate the standard formula described above, the amounts 
reported should be the market value of the principal amount of the underlying or 
of the notional underlying resulting from the prudent valuation guidance set out 
in 
.
CAP50 8

### MAR40.32 .94 defines the vega correlation between risk factors k and l as
40.32

For instruments where the apparent notional amount differs from the 
effective notional amount, banks must use the effective notional 
amount.
8
Futures and forward contracts (including FRAs) are treated as a combination of a 
long and a short position in a notional government security. The maturity of a 
future or an FRA will be the period until delivery or exercise of the contract, plus – 
where applicable – the life of the underlying instrument. For example, a long 
position in a June three-month interest rate future (taken in April) is to be 
reported as a long position in a government security with a five-month maturity 
and a short position in a government security with a two-month maturity. Where 
a range of deliverable instruments may be delivered to fulfil the contract, the 
bank has flexibility to elect which deliverable security goes into the maturity or 
duration ladder but should take account of any conversion factor defined by the 
exchange. In the case of a future on a corporate bond index, positions will be 
included at the market value of the notional underlying portfolio of securities.

### MAR40.33 .94 defines the vega correlation between risk factors k and l as
40.33

Footnotes
Swaps will be treated as two notional positions in government securities with 
relevant maturities. For example, an interest rate swap under which a bank is
receiving floating rate interest and paying fixed will be treated as a long position 
in a floating rate instrument of maturity equivalent to the period until the next 
interest fixing and a short position in a fixed-rate instrument of maturity 
equivalent to the residual life of the swap. For swaps that pay or receive a fixed or 
floating interest rate against some other reference price, eg a stock index, the 
interest rate component should be slotted into the appropriate repricing maturity 
category, with the equity component being included in the equity framework. The 
separate legs of cross-currency swaps are to be reported in the relevant maturity 
ladders for the currencies concerned.

### MAR40.34 .94 defines the vega correlation between risk factors k and l as
40.34

Banks may exclude from the interest rate maturity framework altogether (for both 
specific and general market risk) long and short positions (both actual and 
notional) in identical instruments with exactly the same issuer, coupon, currency 
and maturity. A matched position in a future or forward and its corresponding 
underlying may also be fully offset10 and thus excluded from the calculation. 
When the future or the forward comprises a range of deliverable instruments 
offsetting of positions in the future or forward contract and its underlying is only 
permissible in cases where there is a readily identifiable underlying security that is 
most profitable for the trader with a short position to deliver. The price of this 
security, sometimes called the “cheapest-to-deliver”, and the price of the future 
or forward contract should, in such cases, move in close alignment. No offsetting 
will be allowed between positions in different currencies; the separate legs of 
cross-currency swaps or forward FX deals are to be treated as notional positions 
in the relevant instruments and included in the appropriate calculation for each 
currency.

### MAR40.35 .94 defines the vega correlation between risk factors k and l as
40.35

The leg representing the time to expiry of the future should, however, 
be reported.
10
In addition, opposite positions in the same category of instruments10 can in 
certain circumstances be regarded as matched and allowed to offset fully. To 
qualify for this treatment, the positions must relate to the same underlying 
instruments, be of the same nominal value and be denominated in the same 
currency.11 In addition:

### MAR40.36 .94 defines the vega correlation between risk factors k and l as
40.36

(1)
for futures: offsetting positions in the notional or underlying instruments to 
which the futures contract relates must be for identical products and mature 
within seven days of each other;
Footnotes
(2)
for swaps and FRAs: the reference rate (for floating rate positions) must be 
identical and the coupon closely matched (ie within 15 basis points); and
(3)
for swaps, FRAs and forwards: the next interest fixing date or, for fixed 
coupon positions or forwards, the residual maturity must correspond within 
the following limits:
(a)
less than one month hence: same day;
(b)
between one month and one year hence: within seven days; and
(c)
over one year hence: within 30 days.
This includes the delta-equivalent value of options. The delta 
equivalent of the legs arising out of the treatment of caps and floors as 
set out in 
 can also be offset against each other under the 
MAR40.78
rules laid down in this paragraph.
10
The separate legs of different swaps may also be matched subject to 
the same conditions.
11
Banks with large swap books may use alternative formulae for these swaps to 
calculate the positions to be included in the maturity or duration ladder. One 
method would be to first convert the payments required by the swap into their 
present values. For that purpose, each payment should be discounted using zero 
coupon yields, and a single net figure for the present value of the cash flows 
entered into the appropriate time band using procedures that apply to zero- (or 
low-) coupon bonds; these figures should be slotted into the general market risk 
framework as set out above. An alternative method would be to calculate the 
sensitivity of the net present value implied by the change in yield used in the 
maturity or duration method and allocate these sensitivities into the time bands 
set out in 
 or 
. Other methods which produce similar results 
MAR40.26
MAR40.29
could also be used. Such alternative treatments will, however, only be allowed if:

### MAR40.37 .94 defines the vega correlation between risk factors k and l as
40.37

(1)
the supervisory authority is fully satisfied with the accuracy of the systems 
being used;
(2)
the positions calculated fully reflect the sensitivity of the cash flows to 
interest rate changes and are entered into the appropriate time bands; and
(3)
the positions are denominated in the same currency.
Interest rate and currency swaps, FRAs, forward FX contracts and interest rate 
futures will not be subject to a specific risk charge. This exemption also applies to 
futures on an interest rate index (eg London Interbank Offer Rate, or LIBOR). 
However, in the case of futures contracts where the underlying is a debt security, 
or an index representing a basket of debt securities, a specific risk charge will 
apply according to the credit risk of the issuer as set out in 
 to 
.
MAR40.5
MAR40.21

### MAR40.38 .94 defines the vega correlation between risk factors k and l as
40.38

General market risk applies to positions in all derivative products in the same 
manner as for cash positions, subject only to an exemption for fully or very 
closely matched positions in identical instruments as defined in 
 and 
MAR40.35
. The various categories of instruments should be slotted into the 
MAR40.36
maturity ladder and treated according to the rules identified earlier.

### MAR40.39 .94 defines the vega correlation between risk factors k and l as
40.39

Table 7 presents a summary of the regulatory treatment for interest rate 
derivatives, for market risk purposes.
40.40
Summary of treatment of interest rate derivatives
Table 7
Instrument
Specific risk charge12 
General market risk
charge
Exchanged-traded future
Government debt security
Yes13 
Yes, as two positions
Corporate debt security
Yes
Yes, as two positions
Index on interest rates (eg 
LIBOR)
No
Yes, as two positions
Over-the-counter (OTC) forward
Government debt security
Yes13
Yes, as two positions
Corporate debt security
Yes
Yes, as two positions
Index on interest rates
No
Yes, as two positions
FRAs, swaps
No
Yes, as two positions
Forward FX
No
Yes, as one position 
in each currency
Options
Either
Government debt security
Yes13
(a) carve out together 
with the associated 
hedging positions:
simplified approach; 
scenario analysis; 
internal models
Corporate debt security
Yes
(b) general market 
risk charge according 
to the delta-plus 
method (gamma and 
vega should receive 
separate capital 
requirements)
Index on interest rates
No
FRAs, swaps
No
Footnotes
Equity risk
Specific and general market risks
Equity derivatives
This is the specific risk charge relating to the issuer of the instrument. 
Under the credit risk rules, a separate capital requirement for the 
counterparty credit risk applies.
12
The specific risk capital requirement only applies to government debt 
securities that are rated below AA– (see 
 and 
).
MAR40.6
MAR40.7
13
This section sets out a minimum capital standard to cover the risk of holding or 
taking positions in equities in the trading book. It applies to long and short 
positions in all instruments that exhibit market behaviour similar to equities, but 
not to non-convertible preference shares (which are covered by the interest rate 
risk requirements described in 
 to 
). Long and short positions 
MAR40.3
MAR40.40
in the same issue may be reported on a net basis. The instruments covered 
include common stocks (whether voting or non-voting), convertible securities 
that behave like equities, and commitments to buy or sell equity securities. The 
treatment of derivative products, stock indices and index arbitrage is described in
to 
 below.
MAR40.44
MAR40.52

### MAR40.41 .94 defines the vega correlation between risk factors k and l as
40.41

As with debt securities, the minimum capital standard for equities is expressed in 
terms of two separately calculated capital requirements for the specific risk of 
holding a long or short position in an individual equity and for the general 
market risk of holding a long or short position in the market as a whole. Specific 
risk is defined as the bank’s gross equity positions (ie the sum of all long equity 
positions and of all short equity positions) and general market risk as the 
difference between the sum of the longs and the sum of the shorts (ie the overall 
net position in an equity market).The long or short position in the market must 
be calculated on a market-by-market basis, ie a separate calculation has to be 
carried out for each national market in which the bank holds equities.

### MAR40.42 .94 defines the vega correlation between risk factors k and l as
40.42

The capital requirement for specific risk and for general market risk will each be 
8%.
40.43
Footnotes
Footnotes
Except for options, which are dealt with in 
 to 
, equity 
MAR40.74
MAR40.86
derivatives and off-balance sheet positions that are affected by changes in equity 
prices should be included in the measurement system.14 This includes futures and
swaps on both individual equities and on stock indices. The derivatives are to be 
converted into positions in the relevant underlying. The treatment of equity 
derivatives is summarised in 
 below.
MAR40.52

### MAR40.44 .94 defines the vega correlation between risk factors k and l as
40.44

Where equities are part of a forward contract, a future or an option 
(quantity of equities to be received or to be delivered), any interest rate 
or foreign currency exposure from the other leg of the contract should 
be reported as set out in 
 to 
 and 
 to 
MAR40.3
MAR40.40
MAR40.53
.
MAR40.62
14
In order to calculate the standard formula for specific and general market risk, 
positions in derivatives should be converted into notional equity positions:
40.45
(1)
Futures and forward contracts relating to individual equities should in 
principle be reported at current market prices.
(2)
Futures relating to stock indices should be reported as the marked-to-
market value of the notional underlying equity portfolio.
(3)
Equity swaps are to be treated as two notional positions.15
(4)
Equity options and stock index options should be either carved out together 
with the associated underlyings or be incorporated in the measure of general 
market risk described in this section according to the delta-plus method.
For example, an equity swap in which a bank is receiving an amount 
based on the change in value of one particular equity or stock index 
and paying a different index will be treated as a long position in the 
former and a short position in the latter. Where one of the legs involves 
receiving/paying a fixed or floating interest rate, that exposure should 
be slotted into the appropriate repricing time band for interest rate 
related instruments as set out in 
 to 
. The stock 
MAR40.3
MAR40.40
index should be covered by the equity treatment.
15
Footnotes
Matched positions in each identical equity or stock index in each market may be 
fully offset, resulting in a single net short or long position to which the specific
and general market risk charges will apply. For example, a future in a given equity 
may be offset against an opposite cash position in the same equity.16

### MAR40.46 .94 defines the vega correlation between risk factors k and l as
40.46

The interest rate risk arising out of the future, however, should be 
reported as set out in 
 to 
.
MAR40.3
MAR40.40
16
Besides general market risk, a further capital requirement of 2% will apply to the 
net long or short position in an index contract comprising a diversified portfolio 
of equities. This capital requirement is intended to cover factors such as 
execution risk. National supervisory authorities will take care to ensure that this 
2% risk weight applies only to well-diversified indices and not, for example, to 
sectoral indices.

### MAR40.47 .94 defines the vega correlation between risk factors k and l as
40.47

In the case of the futures-related arbitrage strategies described below, the 
additional 2% capital requirement described above (set out in 
) may be 
MAR40.47
applied to only one index with the opposite position exempt from a capital 
requirement. The strategies are:

### MAR40.48 .94 defines the vega correlation between risk factors k and l as
40.48

(1)
when the bank takes an opposite position in exactly the same index at 
different dates or in different market centres; and
(2)
when the bank has an opposite position in contracts at the same date in 
different but similar indices, subject to supervisory oversight that the two 
indices contain sufficient common components to justify offsetting.
Where a bank engages in a deliberate arbitrage strategy, in which a futures 
contract on a broadly based index matches a basket of stocks, it will be allowed 
to carve out both positions from the simplified standardised approach on 
condition that:

### MAR40.49 .94 defines the vega correlation between risk factors k and l as
40.49

(1)
the trade has been deliberately entered into and separately controlled; and
(2)
the composition of the basket of stocks represents at least 90% of the index 
when broken down into its notional components.
Footnotes
In such a case as set out in 
 the minimum capital requirement will be 
MAR40.49
4% (ie 2% of the gross value of the positions on each side) to reflect divergence 
and execution risks. This applies even if all of the stocks comprising the index are 
held in identical proportions. Any excess value of the stocks comprising the 
basket over the value of the futures contract or excess value of the futures
contract over the value of the basket is to be treated as an open long or short 
position.

### MAR40.50 .94 defines the vega correlation between risk factors k and l as
40.50

If a bank takes a position in depository receipts against an opposite position in 
the underlying equity or identical equities in different markets, it may offset the 
position (ie bear no capital requirement) but only on condition that any costs on 
conversion are fully taken into account.17

### MAR40.51 .94 defines the vega correlation between risk factors k and l as
40.51

Any FX risk arising out of these positions has to be reported as set out 
in 
 to 
.
MAR40.53
MAR40.67
17
Table 8 summarises the regulatory treatment of equity derivatives for market risk 
purposes.
40.52
Summary of treatment of equity derivatives
Table 8
Instrument
Specific risk
18
General market risk
Exchanged-traded or OTC future
Individual equity
Yes 
Yes, as underlying
Index 
2%
Yes, as underlying
Options
Either
Individual equity
Yes
(a) carve out together with the 
associated hedging positions: 
simplified approach; scenario 
analysis; internal models
Index
2%
(b) general market risk charge 
according to the delta-plus 
method (gamma and vega should 
receive separate capital 
requirements)
Footnotes
Foreign exchange risk
Footnotes
Measuring the exposure in a single currency
This is the specific risk charge relating to the issuer of the instrument. 
Under the credit risk rules], a separate capital requirement for the 
counterparty credit risk applies.
18
This section sets out the simplified standardised approach for measuring the risk 
of holding or taking positions in foreign currencies, including gold.19 
40.53
Gold is to be dealt with as an FX position rather than a commodity 
because its volatility is more in line with foreign currencies and banks 
manage it in a similar manner to foreign currencies.
19
Two processes are needed to calculate the capital requirement for FX risk. 
40.54
(1)
The first is to measure the exposure in a single currency position as set out in
to 
. 
MAR40.55
MAR40.58
(2)
The second is to measure the risks inherent in a bank’s mix of long and short 
positions in different currencies as set out in 
 to 
.
MAR40.59
MAR40.62
The bank’s net open position in each currency should be calculated by summing:
40.55
(1)
the net spot position (ie all asset items less all liability items, including 
accrued interest, denominated in the currency in question);
(2)
the net forward position (ie all amounts to be received less all amounts to be 
paid under forward FX transactions, including currency futures and the 
principal on currency swaps not included in the spot position);
(3)
guarantees (and similar instruments) that are certain to be called and are 
likely to be irrecoverable;
(4)
net future income/expenses not yet accrued but already fully hedged (at the 
discretion of the reporting bank);
Footnotes
Footnotes
(5)
any other item representing a profit or loss in foreign currencies (depending 
on particular accounting conventions in different countries); and
(6)
the net delta-based equivalent of the total book of foreign currency options.
20
Subject to a separately calculated capital requirement for gamma and 
vega as described in 
 to 
; alternatively, options and 
MAR40.77
MAR40.80
their associated underlyings are subject to one of the other methods 
described in 
 to 
.
MAR40.74
MAR40.86
20
Positions in composite currencies need to be separately reported but, for 
measuring banks’ open positions, may be either treated as a currency in their 
own right or split into their component parts on a consistent basis. Positions in 
gold should be measured in the same manner as described in 
.
MAR40.68 21

### MAR40.56 .94 defines the vega correlation between risk factors k and l as
40.56

Where gold is part of a forward contract (quantity of gold to be 
received or to be delivered), any interest rate or foreign currency 
exposure from the other leg of the contract should be reported as set 
out in 
 to 
 and 
 above.
MAR40.3
MAR40.40
MAR40.55
21
Interest, other income and expenses should be treated as follows. Interest 
accrued (ie earned but not yet received) should be included as a position. 
Accrued expenses should also be included. Unearned but expected future interest 
and anticipated expenses may be excluded unless the amounts are certain and 
banks have taken the opportunity to hedge them. If banks include future income
/expenses they should do so on a consistent basis, and not be permitted to select 
only those expected future flows which reduce their position.

### MAR40.57 .94 defines the vega correlation between risk factors k and l as
40.57

Forward currency and gold positions should be measured as follows: Forward 
currency and gold positions will normally be valued at current spot market 
exchange rates. Using forward exchange rates would be inappropriate since it 
would result in the measured positions reflecting current interest rate differentials 
to some extent. However, banks that base their normal management accounting 
on net present values are expected to use the net present values of each position, 
discounted using current interest rates and valued at current spot rates, for 
measuring their forward currency and gold positions.

### MAR40.58 .94 defines the vega correlation between risk factors k and l as
40.58

Measuring the foreign exchange risk in a portfolio of foreign currency positions 
and gold
Footnotes
For measuring the FX risk in a portfolio of foreign currency positions and gold as 
set out in 
(2), a bank that is not approved to use internal models by its 
MAR40.54
supervisory authority must use a shorthand method which treats all currencies 
equally.

### MAR40.59 .94 defines the vega correlation between risk factors k and l as
40.59

Under the shorthand method, the nominal amount (or net present value) of the 
net position in each foreign currency and in gold is converted at spot rates into 
the reporting currency.22 The overall net open position is measured by 
aggregating:

### MAR40.60 .94 defines the vega correlation between risk factors k and l as
40.60

(1)
the sum of the net short positions or the sum of the net long positions, 
whichever is the greater;23 plus
(2)
the net position (short or long) in gold, regardless of sign.
Where the bank is assessing its FX risk on a consolidated basis, it may 
be technically impractical in the case of some marginal operations to 
include the currency positions of a foreign branch or subsidiary of the 
bank. In such cases, the internal limit in each currency may be used as 
a proxy for the positions. Provided there is adequate ex post monitoring 
of actual positions against such limits, the limits should be added, 
without regard to sign, to the net open position in each currency.
22
An alternative calculation, which produces an identical result, is to 
include the reporting currency as a residual and to take the sum of all 
the short (or long) positions.
23
The capital requirement will be 8% of the overall net open position (see example 
in Table 9). In particular, the capital requirement would be 8% of the higher of 
either the net long currency positions or the net short currency positions (ie 300) 
and of the net position in gold (35) = 335 x 8% = 26.8.

### MAR40.61 .94 defines the vega correlation between risk factors k and l as
40.61

Commodities risk
Example of the shorthand measure of FX risk
Table 9
JPY
EUR
GBP
CAD
USD
Gold
Net position per 
currency
+50
+100
+150
-20
-180
-35
Net open position
+300
-200
35
A bank of which business in foreign currency is insignificant and which does not 
take FX positions for its own account may, at the discretion of its national 
authority, be exempted from capital requirements on these positions provided 
that:

### MAR40.62 .94 defines the vega correlation between risk factors k and l as
40.62

(1)
its foreign currency business, defined as the greater of the sum of its gross 
long positions and the sum of its gross short positions in all foreign 
currencies, does not exceed 100% of eligible capital as defined in 
; 
CAP10.1
and
(2)
its overall net open position as defined in 
 above does not exceed 
MAR40.60
2% of its eligible capital as defined in 
.
CAP10.1
This section sets out the simplified standardised approach for measuring the risk 
of holding or taking positions in commodities, including precious metals, but 
excluding gold (which is treated as a foreign currency according to the 
methodology set out in 
 to 
 above). A commodity is defined 
MAR40.53
MAR40.62
as a physical product which is or can be traded on a secondary market, eg 
agricultural products, minerals (including oil) and precious metals.

### MAR40.63 .94 defines the vega correlation between risk factors k and l as
40.63

The price risk in commodities is often more complex and volatile than that 
associated with currencies and interest rates. Commodity markets may also be 
less liquid than those for interest rates and currencies and, as a result, changes in 
supply and demand can have a more dramatic effect on price and volatility.24 
These market characteristics can make price transparency and the effective 
hedging of commodities risk more difficult.

### MAR40.64 .94 defines the vega correlation between risk factors k and l as
40.64

Footnotes
Footnotes
Banks need also to guard against the risk that arises when the short 
position falls due before the long position. Owing to a shortage of 
liquidity in some markets, it might be difficult to close the short 
position and the bank might be squeezed by the market.
24
The risks associated with commodities include the following risks:
40.65
(1)
For spot or physical trading, the directional risk arising from a change in the 
spot price is the most important risk.
(2)
However, banks using portfolio strategies involving forward and derivative 
contracts are exposed to a variety of additional risks, which may well be 
larger than the risk of a change in spot prices. These include:
(a)
basis risk (the risk that the relationship between the prices of similar 
commodities alters through time);
(b)
interest rate risk (the risk of a change in the cost of carry for forward 
positions and options); and
(c)
forward gap risk (the risk that the forward price may change for reasons 
other than a change in interest rates).
(3)
In addition, banks may face counterparty credit risk on over-the-counter 
derivatives, but this is captured by the methods set out in 
 to 
 
CRE51
CRE55
and 
.
MAR50
(4)
The funding of commodities positions may well open a bank to interest rate 
or FX exposure and if that is so the relevant positions should be included in 
the measures of interest rate and FX risk described in 
 to 
 
MAR40.3
MAR40.40
and 
 to 
, respectively.
MAR40.53
MAR40.62
25
Where a commodity is part of a forward contract (quantity of 
commodities to be received or to be delivered), any interest rate or 
foreign currency exposure from the other leg of the contract should be 
reported as set out in 
 to 
 and 
 to 
MAR40.3
MAR40.40
MAR40.53
MAR40.
. Positions which are purely stock financing (ie a physical stock has 
62
been sold forward and the cost of funding has been locked in until the 
date of the forward sale) may be omitted from the commodities risk 
calculation although they will be subject to interest rate and 
counterparty risk requirements.
25
Footnotes
Maturity ladder approach
There are two alternatives for measuring commodities position risk under the 
simplified standardised approach that are described in 
 to 
 
MAR40.68
MAR40.73
below. Commodities risk can also be measured, using either (i) the maturity 
ladder approach, which is a measurement system that captures forward gap and 
interest rate risk separately by basing the methodology on seven time bands as 
set out in 
 to 
 below or (ii) the simplified approach, which is a 
MAR40.68
MAR40.71
very simple framework as set out in 
 and 
 below. Both the 
MAR40.72
MAR40.73
maturity ladder approach and the simplified approach are appropriate only for 
banks that, in relative terms, conduct only a limited amount of commodities 
business.

### MAR40.66 .94 defines the vega correlation between risk factors k and l as
40.66

For the maturity ladder approach and the simplified approach, long and short 
positions in each commodity may be reported on a net basis for the purposes of 
calculating open positions. However, positions in different commodities will, as a 
general rule, not be offsettable in this fashion. Nevertheless, national authorities 
will have discretion to permit netting between different subcategories26 of the 
same commodity in cases where the subcategories are deliverable against each 
other. They can also be considered as offsettable if they are close substitutes 
against each other and a minimum correlation of 0.9 between the price 
movements can be clearly established over a minimum period of one year. 
However, a bank wishing to base its calculation of capital requirements for 
commodities on correlations would have to satisfy the relevant supervisory 
authority of the accuracy of the method that has been chosen and obtain its prior 
approval.

### MAR40.67 .94 defines the vega correlation between risk factors k and l as
40.67

Commodities can be grouped into clans, families, subgroups and 
individual commodities. For example, a clan might be Energy 
Commodities, within which Hydro-Carbons are a family with Crude Oil 
being a subgroup and West Texas Intermediate, Arabian Light and 
Brent being individual commodities.
26
In calculating the capital requirements under the maturity ladder approach, banks 
will first have to express each commodity position (spot plus forward) in terms of 
the standard unit of measurement (barrels, kilos, grams etc). The net position in 
each commodity will then be converted at current spot rates into the national 
currency.

### MAR40.68 .94 defines the vega correlation between risk factors k and l as
40.68

Footnotes
Secondly, in order to capture forward gap and interest rate risk within a time 
band (which, together, are sometimes referred to as curvature/spread risk),
matched long and short positions in each time band will carry a capital 
requirement. The methodology is similar to that used for interest rate related 
instruments as set out in 
 to 
. Positions in the separate 
MAR40.3
MAR40.40
commodities (expressed in terms of the standard unit of measurement) will first 
be entered into a maturity ladder while physical stocks should be allocated to the 
first time band. A separate maturity ladder will be used for each commodity as 
defined in 
 above.
MAR40.67
27 For each time band as set out in Table 10, the sum 
of short and long positions that are matched will be multiplied first by the spot 
price for the commodity, and then by the spread rate of 1.5%.

### MAR40.69 .94 defines the vega correlation between risk factors k and l as
40.69

Time bands and spread rates
Table 10
Time band
Spread rate
0-1 month
1.5%
1-3 months
1.5%
3-6 months
1.5%
6-12 months
1.5%
1-2 years
1.5%
2-3 years
1.5%
over 3 years
1.5%
For markets that have daily delivery dates, any contracts maturing 
within 10 days of one another may be offset.
27
The residual net positions from nearer time bands may then be carried forward to 
offset exposures in time bands that are further out. However, recognising that 
such hedging of positions among different time bands is imprecise, a surcharge 
equal to 0.6% of the net position carried forward will be added in respect of each 
time band that the net position is carried forward. The capital requirement for 
each matched amount created by carrying net positions forward will be 
calculated as in 
 above. At the end of this process, a bank will have 
MAR40.69
either only long or only short positions, to which a capital requirement of 15% 
will apply.

### MAR40.70 .94 defines the vega correlation between risk factors k and l as
40.70

All commodity derivatives and off-balance sheet positions that are affected by 
changes in commodity prices should be included in this measurement framework. 
This includes commodity futures, commodity swaps, and options where the 
“delta-plus” method28 is used (see 
 to 
 below). In order to 
MAR40.77
MAR40.80
calculate the risk, commodity derivatives should be converted into notional 
commodities positions and assigned to maturities as follows:

### MAR40.71 .94 defines the vega correlation between risk factors k and l as
40.71

(1)
Futures and forward contracts relating to individual commodities should be 
incorporated as notional amounts of the standard unit of measurement 
(barrels, kilos, grams etc) and should be assigned a maturity with reference 
to expiry date.
(2)
Commodity swaps where one leg is a fixed price and the other the current 
market price should be incorporated as a series of positions equal to the 
notional amount of the contract, with one position corresponding with each 
payment on the swap and slotted into the maturity ladder accordingly. The 
positions would be long positions if the bank is paying fixed and receiving 
floating, and short positions if the bank is receiving fixed and paying floating.
29
(3)
Commodity swaps where the legs are in different commodities are to be 
incorporated in the relevant maturity ladder. No offsetting will be allowed in 
this regard except where the commodities belong to the same subcategory 
as defined in 
 above.
MAR40.67
Footnotes
Simplified approach
Treatment of options
For banks using other approaches to measure options risk, all options 
and the associated underlyings should be excluded from both the 
maturity ladder approach and the simplified approach.
28
If one of the legs involves receiving/paying a fixed or floating interest 
rate, that exposure should be slotted into the appropriate repricing 
maturity band in the maturity ladder covering interest rate related 
instruments.
29
In calculating the capital requirement for directional risk under the simplified 
approach, the same procedure will be adopted as in the maturity ladder 
approach described above (see 
 and 
. Once again, all 
MAR40.68
MAR40.71
commodity derivatives and off-balance sheet positions that are affected by 
changes in commodity prices should be included. The capital requirement will 
equal 15% of the net position, long or short, in each commodity.

### MAR40.72 .94 defines the vega correlation between risk factors k and l as
40.72

In order to protect the bank against basis risk, interest rate risk and forward gap 
risk under the simplified approach, the capital requirement for each commodity 
as described in 
 and 
 above will be subject to an additional 
MAR40.68
MAR40.71
capital requirement equivalent to 3% of the bank’s gross positions, long plus 
short, in that particular commodity. In valuing the gross positions in commodity 
derivatives for this purpose, banks should use the current spot price.

### MAR40.73 .94 defines the vega correlation between risk factors k and l as
40.73

In recognition of the wide diversity of banks’ activities in options and the 
difficulties of measuring price risk for options, two alternative approaches will be 
permissible at the discretion of the national authority under the simplified 
standardised approach.

### MAR40.74 .94 defines the vega correlation between risk factors k and l as
40.74

(1)
Those banks which solely use purchased options30 can use the simplified 
approach described in 
 below;
MAR40.76
Footnotes
Simplified approach
(2)
Those banks which also write options are expected to use the delta-plus 
method or scenario approach which are the intermediate approaches as set 
out in 
 to 
. The more significant its trading activity is, the 
MAR40.77
MAR40.86
more the bank will be expected to use a sophisticated approach, and a bank 
with highly significant trading activity is expected to use the standardised 
approach or the internal models approach as set out in 
 to 
 or 
MAR20
MAR23
 to 
. 
MAR30
MAR33
Unless all their written option positions are hedged by perfectly 
matched long positions in exactly the same options, in which case no 
capital requirement for market risk is required.
30
In the simplified approach for options, the positions for the options and the 
associated underlying, cash or forward, are not subject to the standardised 
methodology but rather are carved-out and subject to separately calculated 
capital requirements that incorporate both general market risk and specific risk. 
The risk numbers thus generated are then added to the capital requirements for 
the relevant category, ie interest rate related instruments, equities, FX and 
commodities as described in 
 to 
. The delta-plus method uses 
MAR40.3
MAR40.73
the sensitivity parameters or Greek letters associated with options to measure 
their market risk and capital requirements. Under this method, the delta-
equivalent position of each option becomes part of the simplified standardised 
approach set out in 
 to 
 with the delta-equivalent amount 
MAR40.3
MAR40.73
subject to the applicable general market risk charges. Separate capital 
requirements are then applied to the gamma and vega risks of the option 
positions. The scenario approach uses simulation techniques to calculate changes 
in the value of an options portfolio for changes in the level and volatility of its 
associated underlyings. Under this approach, the general market risk charge is 
determined by the scenario grid (ie the specified combination of underlying and 
volatility changes) that produces the largest loss. For the delta-plus method and 
the scenario approach, the specific risk capital requirements are determined 
separately by multiplying the delta-equivalent of each option by the specific risk 
weights set out in 
 to 
.
MAR40.3
MAR40.52

### MAR40.75 .94 defines the vega correlation between risk factors k and l as
40.75

Banks that handle a limited range of purchased options can use the simplified 
approach set out in Table 11 for particular trades. As an example of how the 
calculation would work, if a holder of 100 shares currently valued at USD 10 each 
holds an equivalent put option with a strike price of USD 11, the capital 
requirement would be: USD 1,000 x 16% (ie 8% specific plus 8% general market
risk) = USD 160, less the amount the option is in the money (USD 11 - USD 10) x 
100 = USD 100, ie the capital requirement would be USD 60. A similar 
methodology applies for options whose underlying is a foreign currency, an 
interest rate related instrument or a commodity.

### MAR40.76 .94 defines the vega correlation between risk factors k and l as
40.76

Simplified approach: capital requirements
Table 11
Position
Treatment
Long cash and long put
or
short cash and long call
The capital requirement will be the market value of the 
underlying security31 multiplied by the sum of specific 
and general market risk charges32 for the underlying less 
the amount the option is in the money (if any) bounded 
at zero33
Long call
or
long put
The capital requirement will be the lesser of: (i) the 
market value of the underlying security multiplied by 
the sum of specific and general market risk charges32 for 
the underlying and (ii) the market value of the option34
Footnotes
Delta-plus method
In some cases such as FX, it may be unclear which side is the 
underlying security; this should be taken to be the asset that would be 
received if the option were exercised. In addition, the nominal value 
should be used for items where the market value of the underlying 
instrument could be zero, eg caps and floors, swaptions etc.
31
Some options (eg where the underlying is an interest rate, a currency 
or a commodity) bear no specific risk but specific risk will be present in 
the case of options on certain interest rate related instruments (eg 
options on a corporate debt security or corporate bond index; see
to 
 for the relevant capital requirements) and for 
MAR40.3
MAR40.40
options on equities and stock indices (see 
 to 
). The 
MAR40.41
MAR40.52
charge under this measure for currency options will be 8% and for 
options on commodities 15%.
32
For options with a residual maturity of more than six months, the strike 
price should be compared with the forward, not current, price. A bank 
unable to do this must take the in the money amount to be zero.
33
Where the position does not fall within the trading book (ie options on 
certain FX or commodities positions not belonging to the trading book), 
it may be acceptable to use the book value instead.
34
Banks that write options will be allowed to include delta-weighted options 
positions within the simplified standardised approach set out in 
 to 
MAR40.3
. Such options should be reported as a position equal to the market 
MAR40.73
value of the underlying multiplied by the delta. However, since delta does not 
sufficiently cover the risks associated with options positions, banks will also be 
required to measure gamma (which measures the rate of change of delta) and 
vega (which measures the sensitivity of the value of an option with respect to a 
change in volatility) sensitivities in order to calculate the total capital requirement. 
These sensitivities will be calculated according to an approved exchange model 
or to the bank’s proprietary options pricing model subject to oversight by the 
national authority.35

### MAR40.77 .94 defines the vega correlation between risk factors k and l as
40.77

Footnotes
Footnotes
National authorities may wish to require banks doing business in 
certain classes of exotic options (eg barriers, digitals) or in options at 
the money that are close to expiry to use either the scenario approach 
or the internal models alternative, both of which can accommodate 
more detailed revaluation approaches.
35
Delta-weighted positions with debt securities or interest rates as the underlying 
will be slotted into the interest rate time bands, as set out in 
 to 
MAR40.3
MAR40.
, under the following procedure. A two-legged approach should be used as for 
40
other derivatives, requiring one entry at the time the underlying contract takes 
effect and a second at the time the underlying contract matures. For instance, a 
bought call option on a June three-month interest-rate future will in April be 
considered, on the basis of its delta-equivalent value, to be a long position with a 
five-month maturity and a short position with a two-month maturity.36 The 
written option will be similarly slotted as a long position with a two-month 
maturity and a short position with a five-month maturity. Floating rate 
instruments with caps or floors will be treated as a combination of floating rate 
securities and a series of European-style options. For example, the holder of a 
three-year floating rate bond indexed to six month LIBOR with a cap of 15% will 
treat it as:

### MAR40.78 .94 defines the vega correlation between risk factors k and l as
40.78

(1)
a debt security that reprices in six months; and
(2)
a series of five written call options on an FRA with a reference rate of 15%, 
each with a negative sign at the time the underlying FRA takes effect and a 
positive sign at the time the underlying FRA matures.37
A two-month call option on a bond future where delivery of the bond 
takes place in September would be considered in April as being long 
the bond and short a five-month deposit, both positions being delta-
weighted.
36
The rules applying to closely matched positions set out in 
 
MAR40.36
will also apply in this respect.
37
The capital requirement for options with equities as the underlying will also be 
based on the delta-weighted positions that will be incorporated in the measure 
of equity risk described in 
 to 
. For purposes of this 
MAR40.41
MAR40.52
calculation each national market is to be treated as a separate underlying. The 
capital requirement for options on FX and gold positions will be based on the
method for FX rate risk as set out in 
 to 
. For delta risk, the 
MAR40.53
MAR40.62
net delta-based equivalent of the foreign currency and gold options will be 
incorporated into the measurement of the exposure for the respective currency 
(or gold) position. The capital requirement for options on commodities will be 
based on the simplified or the maturity ladder approach for commodities risk as 
set out in 
 to 
. The delta-weighted positions will be 
MAR40.63
MAR40.73
incorporated in one of the measures described in that section.

### MAR40.79 .94 defines the vega correlation between risk factors k and l as
40.79

In addition to the above capital requirements arising from delta risk, there are 
further capital requirements for gamma and vega risk. Banks using the delta-plus 
method will be required to calculate the gamma and vega for each option 
position (including hedge positions) separately. The capital requirements should 
be calculated in the following way:

### MAR40.80 .94 defines the vega correlation between risk factors k and l as
40.80

(1)
For each individual option a gamma impact should be calculated according 
to a Taylor series expansion as follows, where VU is the variation of the 
underlying of the option.
(2)
VU is calculated as follows:
(a)
For interest rate options if the underlying is a bond, the market value of 
the underlying should be multiplied by the risk weights set out in
. An equivalent calculation should be carried out where the 
MAR40.26
underlying is an interest rate, again based on the assumed changes in 
the corresponding yield in 
.
MAR40.26
(b)
For options on equities and equity indices: the market value of the 
underlying should be multiplied by 8%.38
(c)
For FX and gold options: the market value of the underlying should be 
multiplied by 8%.
(d)
For options on commodities: the market value of the underlying should 
be multiplied by 15%.
Footnotes
Scenario approach
(3)
For the purpose of this calculation the following positions should be treated 
as the same underlying:
(a)
for interest rates,39 each time band as set out in 
;
MAR40.26 40
(b)
for equities and stock indices, each national market;
(c)
for foreign currencies and gold, each currency pair and gold; and
(d)
for commodities, each individual commodity as defined in 
.
MAR40.67
(4)
Each option on the same underlying will have a gamma impact that is either 
positive or negative. These individual gamma impacts will be summed, 
resulting in a net gamma impact for each underlying that is either positive or 
negative. Only those net gamma impacts that are negative will be included 
in the capital requirement calculation.
(5)
The total gamma risk capital requirement will be the sum of the absolute 
value of the net negative gamma impacts as calculated above.
(6)
For volatility risk, banks will be required to calculate the capital requirements 
by multiplying the sum of the vega risks for all options on the same 
underlying, as defined above, by a proportional shift in volatility of ± 25%.
(7)
The total capital requirement for vega risk will be the sum of the absolute 
value of the individual capital requirements that have been calculated for 
vega risk.
The basic rules set out here for interest rate and equity options do not 
attempt to capture specific risk when calculating gamma capital 
requirements. However, national authorities may wish to require 
specific banks to do so.
38
Positions have to be slotted into separate maturity ladders by currency.
39
Banks using the duration method should use the time bands as set out 
in 
.
MAR40.29
40
Footnotes
More sophisticated banks may opt to base the market risk capital requirement for 
options portfolios and associated hedging positions on scenario matrix analysis.
This will be accomplished by specifying a fixed range of changes in the option 
portfolio’s risk factors and calculating changes in the value of the option portfolio 
at various points along this grid. For the purpose of calculating the capital 
requirement, the bank will revalue the option portfolio using matrices for 
simultaneous changes in the option’s underlying rate or price and in the volatility 
of that rate or price. A different matrix will be set up for each individual 
underlying as defined in 
 above. As an alternative, at the discretion of 
MAR40.80
each national authority, banks that are significant traders in options will for 
interest rate options be permitted to base the calculation on a minimum of six 
sets of time bands. When using this method, not more than three of the time 
bands as defined in 
 and 
 should be combined into any one 
MAR40.26
MAR40.29
set.

### MAR40.81 .94 defines the vega correlation between risk factors k and l as
40.81

The options and related hedging positions will be evaluated over a specified 
range above and below the current value of the underlying. The range for interest 
rates is consistent with the assumed changes in yield in 
. Those banks 
MAR40.26
using the alternative method for interest rate options set out in 
 above 
MAR40.81
should use, for each set of time bands, the highest of the assumed changes in 
yield applicable to the group to which the time bands belong.41 The other ranges 
are ± 8% for equities,42 ± 8% for FX and gold, and ± 15% for commodities. For all 
risk categories, at least seven observations (including the current observation) 
should be used to divide the range into equally spaced intervals.

### MAR40.82 .94 defines the vega correlation between risk factors k and l as
40.82

If, for example, the time bands 3 to 4 years, 4 to 5 years and 5 to 7 
years are combined the highest assumed change in yield of these three 
bands would be 0.75.
41
The basic rules set out here for interest rate and equity options do not 
attempt to capture specific risk when calculating gamma capital 
requirements. However, national authorities may wish to require 
specific banks to do so.
42
The second dimension of the matrix entails a change in the volatility of the 
underlying rate or price. A single change in the volatility of the underlying rate or 
price equal to a shift in volatility of + 25% and - 25% is expected to be sufficient 
in most cases. As circumstances warrant, however, the supervisory authority may 
choose to require that a different change in volatility be used and/or that 
intermediate points on the grid be calculated.

### MAR40.83 .94 defines the vega correlation between risk factors k and l as
40.83

After calculating the matrix, each cell contains the net profit or loss of the option 
and the underlying hedge instrument. The capital requirement for each 
underlying will then be calculated as the largest loss contained in the matrix.

### MAR40.84 .94 defines the vega correlation between risk factors k and l as
40.84

The application of the scenario analysis by any specific bank will be subject to 
supervisory consent, particularly as regards the precise way that the analysis is 
constructed. Banks’ use of scenario analysis as part of the simplified standardised 
approach will also be subject to validation by the national authority, and to those 
of the qualitative standards for internal models as set out in 
.
MAR30

### MAR40.85 .94 defines the vega correlation between risk factors k and l as
40.85

Besides the options risks mentioned above, the Committee is conscious of the 
other risks also associated with options, eg rho (rate of change of the value of the 
option with respect to the interest rate) and theta (rate of change of the value of 
the option with respect to time). While not proposing a measurement system for 
those risks at present, it expects banks undertaking significant options business at 
the very least to monitor such risks closely. Additionally, banks will be permitted 
to incorporate rho into their capital calculations for interest rate risk, if they wish 
to do so.

### MAR40.86 .94 defines the vega correlation between risk factors k and l as
40.86


## MAR50 .94 defines the vega correlation between risk factors k and l as

Credit valuation adjustment 
framework
This chapter sets out how to calculate capital 
requirements to cover credit valuation 
adjustment risk.
Version effective as of
01 Jan 2023
Changes to give effect to the target revisions to 
the CVA framework published on the 8 July 2020.
Definitions and application
The risk-weighted assets for credit value adjustment risk are determined by 
multiplying the capital requirements calculated as set out in this chapter by 12.5.
50.1
In the context of this document, CVA stands for credit valuation adjustment 
specified at a counterparty level. CVA reflects the adjustment of default risk-free 
prices of derivatives and securities financing transactions (SFTs) due to a potential 
default of the counterparty.

### MAR50.2 .94 defines the vega correlation between risk factors k and l as
50.2

Unless explicitly specified otherwise, the term CVA in this document means 
regulatory CVA. Regulatory CVA may differ from CVA used for accounting 
purposes as follows:

### MAR50.3 .94 defines the vega correlation between risk factors k and l as
50.3

(1)
regulatory CVA excludes the effect of the bank’s own default; and
(2)
several constraints reflecting best practice in accounting CVA are imposed 
on calculations of regulatory CVA. .
CVA risk is defined as the risk of losses arising from changing CVA values in 
response to changes in counterparty credit spreads and market risk factors that 
drive prices of derivative transactions and SFTs.

### MAR50.4 .94 defines the vega correlation between risk factors k and l as
50.4

The capital requirements for CVA risk must be calculated by all banks involved in 
covered transactions in both banking book and trading book. Covered 
transactions include:

### MAR50.5 .94 defines the vega correlation between risk factors k and l as
50.5

(1)
all derivatives except those transacted directly with a qualified central 
counterparty and except those transactions meeting the conditions of CRE54.
to 
; and 
14
CRE54.16
(2)
SFTs that are fair-valued by a bank for accounting purposes, if their 
supervisor determines that the bank's CVA loss exposures arising from SFT 
transactions are material. In case the bank deems the exposures immaterial, 
the bank must justify its assessment to its supervisory by providing relevant 
supporting documentation.
Footnotes
FAQ
Are SFTs for which the accounting amount of CVA reserves is 
determined to be zero included in the scope of “SFTs that are fair-
valued by a bank for accounting purposes”?
For the purpose of CVA capital requirement, SFTs that are fair-valued 
for accounting purposes and for which a bank records zero for CVA 
reserves for accounting purposes are included in the scope of covered 
transactions if the CVA risk of those SFTs is deemed material as 
described in 
 (2).
MAR50.5
FAQ1
The CVA risk capital requirements are calculated for a bank’s “CVA portfolio” on a 
standalone basis. The CVA portfolio includes CVA for a bank’s entire portfolio of 
covered transactions and eligible CVA hedges.

### MAR50.6 .94 defines the vega correlation between risk factors k and l as
50.6

Two approaches are available for calculating CVA capital requirements: the 
standardised approach (SA-CVA) and the basic approach (BA-CVA). Banks must 
use the BA-CVA unless they receive approval from their relevant supervisory 
authority to use the SA-CVA.1

### MAR50.7 .94 defines the vega correlation between risk factors k and l as
50.7

Note that this is in contrast to the application of the market risk 
approaches set out in 
, where banks do not need supervisory 
MAR11
approval to use the standardised approach.
1
Banks that have received approval of their supervisory authority to use the SA-
CVA may carve out from the SA-CVA calculations any number of netting sets. 
CVA capital requirements for all carved-out netting sets must be calculated using 
the BA-CVA. When applying the carve-out, a legal netting set may also be split 
into two synthetic netting sets, one containing the carved-out transactions 
subject to the BA-CVA and the other subject to the SA-CVA, subject to one or 
both of the following conditions:

### MAR50.8 .94 defines the vega correlation between risk factors k and l as
50.8

(1)
the split is consistent with the treatment of the legal netting set used by the 
bank for calculating accounting CVA (eg where certain transactions are not 
processed by the front office/accounting exposure model); or
(2)
supervisory approval to use the SA-CVA is limited and does not cover all 
transactions within a legal netting set.
Banks that are below the materiality threshold specified in 
(1) may opt 
MAR50.9
not to calculate its CVA capital requirements using the SA-CVA or BA-CVA and 
instead choose an alternative treatment.

### MAR50.9 .94 defines the vega correlation between risk factors k and l as
50.9

(1)
Any bank whose aggregate notional amount of non-centrally cleared 
derivatives is less than or equal to 100 billion euro is deemed as being below 
the materiality threshold.
(2)
Any bank below the materiality threshold may choose to set its CVA capital 
requirement equal to 100% of the bank’s capital requirement for 
counterparty credit risk (CCR).
(3)
CVA hedges are not recognised under this treatment.
(4)
If chosen, this treatment must be applied to the bank’s entire portfolio 
instead of the BA-CVA or the SA-CVA.
(5)
A bank’s relevant supervisory authority, however, can remove this option if it 
determines that CVA risk resulting from the bank’s derivative positions 
materially contributes to the bank’s overall risk.
Eligibility criteria for CVA hedges are specified in 
 to 
 for the 
MAR50.17
MAR50.19
BA-CVA and in 
 to 
 for the SA-CVA.
MAR50.37
MAR50.39
50.10
CVA hedging instruments can be external (ie with an external counterparty) or 
internal (ie with one of the bank’s trading desks).
50.11
(1)
All external CVA hedges (including both eligible and ineligible external CVA 
hedges) that are covered transactions must be included in the CVA 
calculation of the counterparty providing to the hedge.
(2)
All eligible external CVA hedges must be excluded from a bank’s market risk 
capital requirement calculations under 
 through 
.
MAR10
MAR40
(3)
Ineligible external CVA hedges are treated as trading book instruments and 
are capitalised under 
 through 
.
MAR10
MAR40
Basic approach for credit valuation adjustment risk
(4)
An internal CVA hedge involves two perfectly offsetting positions: one of the 
CVA desk and the opposite position of the trading desk:
(a)
If an internal CVA hedge is ineligible, both positions belong to the 
trading book where they cancel each other, so there is no impact on 
either the CVA portfolio or the trading book.
(b)
If an internal CVA hedge is eligible, the CVA desk’s position is part of 
the CVA portfolio where it is capitalised as set out in this chapter, while 
the trading desk’s position is part of the trading book where it is 
capitalised as set out in 
 through 
.
MAR10
MAR40
(5)
If an internal CVA hedge involves an instrument that is subject to curvature 
risk, default risk charge or the residual risk add-on under the standardised 
approach as set out in 
 to 
, it can be eligible only if the trading 
MAR20
MAR23
desk that is the CVA desk’s internal counterparty executes a transaction with 
an external counterparty that exactly offsets the trading desk’s position with 
the CVA desk.
Banks that use the BA-CVA or the SA-CVA for calculating CVA capital 
requirements may cap the maturity adjustment factor at 1 for all netting sets 
contributing to CVA capital requirements when they calculate CCR capital 
requirements under the Internal Ratings Based (IRB) approach.

### MAR50.12 .94 defines the vega correlation between risk factors k and l as
50.12

The BA-CVA calculations may be performed either via the reduced version or the 
full version. A bank under the BA-CVA approach can choose whether to 
implement the full version or the reduced version at its discretion. However, all 
banks using the BA-CVA must calculate the reduced version of BA-CVA capital 
requirements as the reduced BA-CVA is also part of the full BA-CVA capital 
calculations as a conservative means to limit hedging recognition.

### MAR50.13 .94 defines the vega correlation between risk factors k and l as
50.13

(1)
The full version recognises counterparty credit spread hedges and is 
intended for banks that hedge CVA risk.
(2)
The reduced version eliminates the element of hedging recognition from the 
full version. The reduced version is designed to simplify BA-CVA 
implementation for less sophisticated banks that do not hedge CVA.
Reduced version of the BA-CVA (hedges are not recognised)
Footnotes
The capital requirements for CVA risk under the reduced version of the BA-CVA 
(DS
 × K
, where the discount scalar DS
 = 0.65) are calculated 
BA-CVA
reduced
BA-CVA
as follows (where the summations are taken over all counterparties that are 
within scope of the CVA charge), where:

### MAR50.14 .94 defines the vega correlation between risk factors k and l as
50.14

(1)
SCVA is the CVA capital requirement that counterparty c would receive if 
c
considered on a stand-alone basis (referred to as "stand-alone CVA capital" 
below). See 
 for its calculation;
MAR50.15
(2)
ρ = 50%. It is the supervisory correlation parameter. Its square, ρ2=25%, 
represents the correlation between credit spreads of any two counterparties.2
In the formula below, the effect of ρ is to recognise the fact that the CVA risk 
to which a bank is exposed is less than the sum of the CVA risk for each 
counterparty, given that the credit spreads of counterparties are typically not 
perfectly correlated; and
(3)
The first term under the square root in the formula below aggregates the 
systematic components of CVA risk, and the second term under the square 
root aggregates the idiosyncratic components of CVA risk.
One of the basic assumptions underlying the BA-CVA is that systematic 
credit spread risk is driven by a single factor. Under this assumption, ρ 
can be interpreted as the correlation between the credit spread of a 
counterparty and the single credit spread systematic factor.
2
The stand-alone CVA capital requirements for counterparty c that are used in the 
formula in 
 (SCVA ) are calculated as follows (where the summation is 
MAR50.14
c
across all netting sets with the counterparty), where:

### MAR50.15 .94 defines the vega correlation between risk factors k and l as
50.15

(1)
RW is the risk weight for counterparty c that reflects the volatility of its 
c
credit spread. These risk weights are based on a combination of sector and 
credit quality of the counterparty as prescribed in 
.
MAR50.16
Footnotes
(2)
M
 is the effective maturity for the netting set NS. For banks that have 
NS
supervisory approval to use the IMM, M
 is calculated as per 
 and 
NS
CRE53.20
, with the exception that the five year cap in 
 is not 
CRE53.21
CRE53.20
applied. For banks that do not have supervisory approval to use the IMM, M
is calculated according to 
 to 
, with the exception that 
NS
CRE32.46
CRE32.54
the five-year cap in 
 is not applied.
CRE32.46
(3)
EAD
 is the exposure at default (EAD) of the netting set NS, calculated in 
NS
the same way as the bank calculates it for minimum capital requirements for 
CCR.
(4)
DF
 is a supervisory discount factor. It is 1 for banks using the IMM to 
NS
calculate EAD, and is
 for banks not using the IMM.3
(5)
α = 1.4.4
DF is the supervisory discount factor averaged over time between today 
and the netting set's effective maturity date. The interest rate used for 
discounting is set at 5%, hence 0.05 in the formula. The product of EAD 
and effective maturity in the BA-CVA formula is a proxy for the area 
under the discounted expected exposure profile of the netting set. The 
IMM definition of effective maturity already includes this discount 
factor, hence DF is set to 1 for IMM banks. Outside IMM, the netting set’
s effective maturity is defined as an average of actual trade maturities. 
This definition lacks discounting, so the supervisory discount factor is 
added to compensate for this.
3
α is the multiplier used to convert Effective expected positive exposure 
(EEPE) to EAD in both SA-CCR and IMM. Its role in the calculation, 
therefore, is to convert the EAD of the netting set (EAD
) back to EEPE.
NS
4
Full version of the BA-CVA (hedges are recognised)
The supervisory risk weights (RW ) are given in Table 1. Credit quality is specified 
C
as either investment grade (IG), high yield (HY), or not rated (NR). Where there
are no external ratings or where external ratings are not recognised within a 
jurisdiction, banks may, subject to supervisory approval, map the internal rating 
to an external rating and assign a risk weight corresponding to either IG or HY. 
Otherwise, the risk weights corresponding to NR is to be applied.

### MAR50.16 .94 defines the vega correlation between risk factors k and l as
50.16

Supervisory risk weights, RW­C
Table 1
Sector of counterparty
Credit quality of
counterparty
IG
HY and NR
Sovereigns including central banks and multilateral 
development banks
0.5%
2.0%
Local government, government-backed non-financials, 
education and public administration
1.0%
4.0%
Financials including government-backed financials
5.0%
12.0%
Basic materials, energy, industrials, agriculture, 
manufacturing, mining and quarrying
3.0%
7.0%
Consumer goods and services, transportation and storage, 
administrative and support service activities
3.0%
8.5%
Technology, telecommunications
2.0%
5.5%
Health care, utilities, professional and technical activities
1.5%
5.0%
Other sector
5.0%
12.0%
As set out in 
(1) the full version of the BA-CVA recognises the effect of 
MAR50.13
counterparty credit spread hedges. Only transactions used for the purpose of 
mitigating the counterparty credit spread component of CVA risk, and managed 
as such, can be eligible hedges.

### MAR50.17 .94 defines the vega correlation between risk factors k and l as
50.17

Only single-name credit default swaps (CDS), single-name contingent CDS and 
index CDS can be eligible CVA hedges.
50.18
Eligible single-name credit instruments must: 
50.19
(1)
reference the counterparty directly; or
(2)
reference an entity legally related to the counterparty, where legally related 
refers to cases where the reference name and the counterparty are either a 
parent and its subsidiary or two subsidiaries of a common parent; or
(3)
reference an entity that belongs to the same sector and region as the 
counterparty.
Banks that intend to use the full version of BA-CVA must calculate the reduced 
version (K
) as well. Under the full version, capital requirements for CVA risk 
reduced
DS
 × K
 is calculated as follows, where DS
 =0.65, and β=0.25 is the 
BA-CVA
full
BA-CVA
supervisory parameter that is used to provide a floor that limits the extent to 
which hedging can reduce the capital requirements for CVA risk:

### MAR50.20 .94 defines the vega correlation between risk factors k and l as
50.20

The part of capital requirements that recognises eligible hedges (K
) is 
hedged
calculated as follows (where the summations are taken over all counterparties c 
that are within scope of the CVA charge), where:

### MAR50.21 .94 defines the vega correlation between risk factors k and l as
50.21

(1)
Both the stand-alone CVA capital (SCVA ) and the correlation parameter (ρ) 
C
are defined in exactly the same way as for the reduced version calculation of 
the BA-CVA.
(2)
SNH is a quantity that gives recognition to the reduction in CVA risk of the 
C
counterparty c arising from the bank’s use of single-name hedges of credit 
spread risk. See 
 for its calculation.
MAR50.23
(3)
IH is a quantity that gives recognition to the reduction in CVA risk across all 
counterparties arising from the bank’s use of index hedges. See 
 
MAR50.24
for its calculation.
(4)
HMA is a quantity characterising hedging misalignment, which is designed to 
C
limit the extent to which indirect hedges can reduce capital requirements given
that they will not fully offset movements in a counterparty’s credit spread. That
is, with indirect hedges present, K
 cannot reach zero. See 
 for 
hedged
MAR50.25
its calculation.
The formula for K
 in 
 comprises three main terms as below:
hedged
MAR50.21
50.22
(1)
The first term
 aggregates the systematic
components of CVA risk arising from the bank’s counterparties, the single-
name hedges and the index hedges.
(2)
The second term
 aggregates the idiosyncratic
components of CVA risk arising from the bank’s counterparties and the 
single-name hedges.
(3)
The third term
 aggregates the components of indirect hedges that
are not aligned with counterparties’ credit spreads.
The quantity SNH is calculated as follows (where the summation is across all 
c
single name hedges h that the bank has taken out to hedge the CVA risk of 
counterparty c), where:

### MAR50.23 .94 defines the vega correlation between risk factors k and l as
50.23

(1)
r
 is the supervisory prescribed correlation between the credit spread of 
hc
counterparty c and the credit spread of a single-name hedge h of 
counterparty c. The value of r
 is set out in the Table 2 of 
. It is set 
hc
MAR50.26
at 100% if the hedge directly references the counterparty c, and set at lower 
values if it does not.
(2)
 is the remaining maturity of single-name hedge h.
(3)
 is the notional of single-name hedge h. For single-name contingent
CDS, the notional is determined by the current market value of the reference 
portfolio or instrument.
(4)
 is the supervisory discount factor calculated as
 .
(5)
RW is the supervisory risk weight of single-name hedge h that reflects the 
h
volatility of the credit spread of the reference name of the hedging 
instrument. These risk weights are based on a combination of the sector and 
the credit quality of the reference name of the hedging instrument as 
prescribed in Table 1 of 
.
MAR50.16
The quantity IH is calculated as follows (where the summation is across all index 
hedges i that the bank has taken out to hedge CVA risk), where:
50.24
(1)
 is the remaining maturity of index hedge i.
(2)
 is the notional of the index hedge i.
(3)
 is the supervisory discount factor calculated as
(4)
RW is the supervisory risk weight of the index hedge i. RW is taken from the 
i
i
Table 1 of 
 based on the sector and the credit quality of the index 
MAR50.16
constituents and adjusted as follows:
(a)
For an index where all index constituents belong to the same sector and 
are of the same credit quality, the relevant value in the Table 1 of
is multiplied by 0.7 to account for diversification of 
MAR50.16
idiosyncratic risk within the index.
(b)
For an index spanning multiple sectors or with a mixture of investment 
grade constituents and other grade constituents, the name-weighted 
average of the risk weights from the Table 1 of 
 should be 
MAR50.16
calculated and then multiplied by 0.7.
Standardised approach for credit valuation adjustment risk
The quantity HMA is calculated as follows (where the summation is across all 
C
single name hedges h that have been taken out to hedge the CVA risk of
counterparty c), where
 and RW have the same definitions as 
h
set out in 
.
MAR50.23

### MAR50.25 .94 defines the vega correlation between risk factors k and l as
50.25

The supervisory prescribed correlations 
 between the credit spread of 
rhc
counterparty  and the credit spread of its single-name hedge  are set in Table 2 
c
h
as follows:

### MAR50.26 .94 defines the vega correlation between risk factors k and l as
50.26

Correlations between credit spread of counterparty and single-name hedge
Table 2
Single-name hedge h of counterparty c
Value of rhc
references counterparty c directly
100%
has legal relation with counterparty c
80%
shares sector and region with counterparty c
50%
The SA-CVA is an adaptation of the standardised approach for market risk set out 
in 
 to 
. The primary differences of the SA-CVA from the 
MAR20
MAR23
standardised approach for market risk are:

### MAR50.27 .94 defines the vega correlation between risk factors k and l as
50.27

(1)
the SA-CVA features a reduced granularity of market risk factors; and
(2)
the SA-CVA does not include default risk and curvature risk.
Under the SA-CVA, capital requirements must be calculated and reported to 
supervisors at the same monthly frequency as for the market risk standardised 
approach. In addition, banks using the SA-CVA must have the ability to produce 
SA-CVA capital requirement calculations at the request of their supervisors and 
must accordingly provide the calculations.

### MAR50.28 .94 defines the vega correlation between risk factors k and l as
50.28

Regulatory CVA calculations
The SA-CVA uses as inputs the sensitivities of regulatory CVA to counterparty 
credit spreads and market risk factors driving the values of covered transactions.
Sensitivities must be computed by banks in accordance with the prudent 
valuation standards set out in 
.
CAP50

### MAR50.29 .94 defines the vega correlation between risk factors k and l as
50.29

For a bank to be considered eligible for the use of SA-CVA by its relevant 
supervisor as set out in 
, the bank must meet the following criteria at the 
MAR50.7
minimum.

### MAR50.30 .94 defines the vega correlation between risk factors k and l as
50.30

(1)
A bank must be able to model exposure and calculate, on at least a monthly 
basis, CVA and CVA sensitivities to the market risk factors specified in MAR50.
to 
.
54
MAR50.77
(2)
A bank must have a CVA desk (or a similar dedicated function) responsible 
for risk management and hedging of CVA.
A bank must calculate regulatory CVA for each counterparty with which it has at 
least one covered position for the purpose of the CVA risk capital requirements.
50.31
Regulatory CVA at a counterparty level must be calculated according to the 
following principles. A bank must demonstrate its compliance to the principles to 
its relevant supervisor.

### MAR50.32 .94 defines the vega correlation between risk factors k and l as
50.32

(1)
Regulatory CVA must be calculated as the expectation of future losses 
resulting from default of the counterparty under the assumption that the 
bank itself is free from the default risk. In expressing the regulatory CVA, non-
zero losses must have a positive sign. This is reflected in 
 where 
MAR50.52
must be subtracted from
.
(2)
The calculation must be based on at least the following three sets of inputs:
(a)
term structure of market-implied probability of default (PD);
(b)
market-consensus expected loss-given-default (ELGD);
(c)
simulated paths of discounted future exposure.
(3)
The term structure of market-implied PD must be estimated from credit 
spreads observed in the markets. For counterparties whose credit is not 
actively traded (ie illiquid counterparties), the market-implied PD must be
estimated from proxy credit spreads estimated for these counterparties 
according to the following requirements:
(a)
A bank must estimate the credit spread curves of illiquid counterparties 
from credit spreads observed in the markets of the counterparty's liquid 
peers via an algorithm that discriminates on at least the following three 
variables: a measure of credit quality (eg rating), industry, and region.
(b)
In certain cases, mapping an illiquid counterparty to a single liquid 
reference name can be allowed. A typical example would be mapping a 
municipality to its home country (ie setting the municipality credit 
spread equal to the sovereign credit spread plus a premium). A bank 
must justify to its supervisor each case of mapping an illiquid 
counterparty to a single liquid reference name.
(c)
When no credit spreads of any of the counterparty's peers is available 
due to the counterparty's specific type (eg project finance, funds), a 
bank is allowed to use a more fundamental analysis of credit risk to 
proxy the spread of an illiquid counterparty. However, where historical 
PDs are used as part of this assessment, the resulting spread cannot be 
based on historical PD only - it must relate to credit markets.
(4)
The market-consensus ELGD value must be the same as the one used to 
calculate the risk-neutral PD from credit spreads unless the bank can 
demonstrate that the seniority of the exposure resulting from covered 
positions differs from the seniority of senior unsecured bonds. Collateral 
provided by the counterparty does not change the seniority of the exposure.
(5)
The simulated paths of discounted future exposure are produced by pricing 
all derivative transactions with the counterparty along simulated paths of 
relevant market risk factors and discounting the prices to today using risk-
free interest rates along the path.
(6)
All market risk factors material for the transactions with a counterparty must 
be simulated as stochastic processes for an appropriate number of paths 
defined on an appropriate set of future time points extending to the 
maturity of the longest transaction.
(7)
For transactions with a significant level of dependence between exposure 
and the counterparty's credit quality, this dependence should be taken into 
account.
(8)
For margined counterparties, collateral is permitted to be recognised as a 
risk mitigant under the following conditions:
(a)
Collateral management requirements outlined in 
 and 
CRE53.39
CRE53.40
are satisfied.
(b)
All documentation used in collateralised transactions must be binding 
on all parties and legally enforceable in all relevant jurisdictions. Banks 
must have conducted sufficient legal review to verify this and have a 
well founded legal basis to reach this conclusion, and undertake such 
further review as necessary to ensure continuing enforceability.
(9)
For margined counterparties, the simulated paths of discounted future 
exposure must capture the effects of margining collateral that is recognised 
as a risk mitigant along each exposure path. All the relevant contractual 
features such as the nature of the margin agreement (unilateral vs bilateral), 
the frequency of margin calls, the type of collateral, thresholds, independent 
amounts, initial margins and minimum transfer amounts must be 
appropriately captured by the exposure model. To determine collateral 
available to a bank at a given exposure measurement time point, the 
exposure model must assume that the counterparty will not post or return 
any collateral within a certain time period immediately prior to that time 
point. The assumed value of this time period, known as the margin period of 
risk (MPoR), cannot be less than a supervisory floor. For SFTs and client 
cleared transactions as specified in 
, the supervisory floor for the 
CRE54.12
MPoR is equal to 4+N business days, where N is the re-margining period 
specified in the margin agreement (in particular, for margin agreements with 
daily or intra-daily exchange of margin, the minimum MPoR is 5 business 
days). For all other transactions, the supervisory floor for the MPoR is equal 
to 9+N business days.
The simulated paths of discounted future exposure are obtained via the exposure 
models used by a bank for calculating front office/accounting CVA, adjusted (if 
needed) to meet the requirements imposed for regulatory CVA calculation. 
Model calibration process (with the exception of the MPoR), market and 
transaction data used for regulatory CVA calculation must be the same as the 
ones used for accounting CVA calculation.

### MAR50.33 .94 defines the vega correlation between risk factors k and l as
50.33

The generation of market risk factor paths underlying the exposure models must 
satisfy and a bank must demonstrate to its relevant supervisors its compliance to 
the following requirements:

### MAR50.34 .94 defines the vega correlation between risk factors k and l as
50.34

(1)
Drifts of risk factors must be consistent with a risk-neutral probability 
measure. Historical calibration of drifts is not allowed.
(2)
The volatilities and correlations of market risk factors must be calibrated to 
market data whenever sufficient data exist in a given market. Otherwise, 
historical calibration is permissible.
(3)
The distribution of modelled risk factors must account for the possible non-
normality of the distribution of exposures, including the existence of 
leptokurtosis (“fat tails”), where appropriate.
Netting recognition is the same as in the accounting CVA calculations used by 
the bank. In particular, netting uncertainty can be modelled.
50.35
A bank must satisfy and demonstrate to its relevant supervisors its compliance to 
the following requirements:
50.36
(1)
Exposure models used for calculating regulatory CVA must be part of a CVA 
risk management framework that includes the identification, measurement, 
management, approval and internal reporting of CVA risk. A bank must have 
a credible track record in using these exposure models for calculating CVA 
and CVA sensitivities to market risk factors.
(2)
Senior management should be actively involved in the risk control process 
and must regard CVA risk control as an essential aspect of the business to 
which significant resources need to be devoted.
(3)
A bank must have a process in place for ensuring compliance with a 
documented set of internal policies, controls and procedures concerning the 
operation of the exposure system used for accounting CVA calculations.
(4)
A bank must have an independent control unit that is responsible for the 
effective initial and ongoing validation of the exposure models. This unit 
must be independent from business credit and trading units (including the 
CVA desk), must be adequately staffed and must report directly to senior 
management of the bank.
(5)
A bank must document the process for initial and ongoing validation of its 
exposure models to a level of detail that would enable a third party to 
understand how the models operate, their limitations, and their key 
assumptions; and recreate the analysis. This documentation must set out the 
minimum frequency with which ongoing validation will be conducted as well 
as other circumstances (such as a sudden change in market behaviour) under 
which additional validation should be conducted. In addition, the 
documentation must describe how the validation is conducted with respect 
to data flows and portfolios, what analyses are used and how representative 
counterparty portfolios are constructed.
Eligible hedges
(6)
The pricing models used to calculate exposure for a given path of market 
risk factors must be tested against appropriate independent benchmarks for 
a wide range of market states as part of the initial and ongoing model 
validation process. Pricing models for options must account for the non-
linearity of option value with respect to market risk factors.
(7)
An independent review of the overall CVA risk management process should 
be carried out regularly in the bank’s own internal auditing process. This 
review should include both the activities of the CVA desk and of the 
independent risk control unit.
(8)
A bank must define criteria on which to assess the exposure models and 
their inputs and have a written policy in place to describe the process to 
assess the performance of exposure models and remedy unacceptable 
performance.
(9)
Exposure models must capture transaction-specific information in order to 
aggregate exposures at the level of the netting set. A bank must verify that 
transactions are assigned to the appropriate netting set within the model.
(10)
Exposure models must reflect transaction terms and specifications in a 
timely, complete, and conservative fashion. The terms and specifications 
must reside in a secure database that is subject to formal and periodic 
audit. The transmission of transaction terms and specifications data to the 
exposure model must also be subject to internal audit, and formal 
reconciliation processes must be in place between the internal model and 
source data systems to verify on an ongoing basis that transaction terms 
and specifications are being reflected in the exposure system correctly or at 
least conservatively.
(11)
The current and historical market data must be acquired independently of 
the lines of business and be compliant with accounting. They must be fed 
into the exposure models in a timely and complete fashion, and maintained 
in a secure database subject to formal and periodic audit. A bank must also 
have a well-developed data integrity process to handle the data of 
erroneous and/or anomalous observations. In the case where an exposure 
model relies on proxy market data, a bank must set internal policies to 
identify suitable proxies and the bank must demonstrate empirically on an 
ongoing basis that the proxy provides a conservative representation of the 
underlying risk under adverse market conditions.
Multiplier
Calculations
Only whole transactions that are used for the purpose of mitigating CVA risk, and 
managed as such, can be eligible hedges. Transactions cannot be split into 
several effective transactions.

### MAR50.37 .94 defines the vega correlation between risk factors k and l as
50.37

Eligible hedges can include: 
50.38
(1)
instruments that hedge variability of the counterparty credit spread; and
(2)
instruments that hedge variability of the exposure component of CVA risk.
Instruments that are not eligible for the internal models approach for market risk 
under 
 to 
 (eg tranched credit derivatives) cannot be eligible CVA 
MAR30
MAR33
hedges.

### MAR50.39 .94 defines the vega correlation between risk factors k and l as
50.39

Aggregated capital requirements can be scaled up by the multiplier m
.
CVA
50.40
The multiplier m
 is set at 1. A bank's relevant supervisor may require a bank to 
CVA
use a higher value of m
 if the supervisor determines that the bank's CVA 
CVA
model risk warrants it (eg if the level of model risk for the calculation of CVA 
sensitivities is too high or the dependence between the bank's exposure to a 
counterparty and the counterparty's credit quality is not appropriately taken into 
account in its CVA calculations).

### MAR50.41 .94 defines the vega correlation between risk factors k and l as
50.41

The SA-CVA capital requirements are calculated as the sum of the capital 
requirements for delta and vega risks calculated for the entire CVA portfolio 
(including eligible hedges).

### MAR50.42 .94 defines the vega correlation between risk factors k and l as
50.42

The capital requirements for delta risk are calculated as the simple sum of delta 
capital requirements calculated independently for the following six risk classes: 
50.43
(1)
interest rate risk;
(2)
foreign exchange (FX) risk;
(3)
counterparty credit spread risk;
(4)
reference credit spread risk (ie credit spreads that drive the CVA exposure 
component);
(5)
equity risk; and
(6)
commodity risk.
If an instrument is deemed as an eligible hedge for credit spread delta risk, it 
must be assigned in its entirety (see 
) either to the counterparty credit 
MAR50.37
spread or to the reference credit spread risk class. Instruments must not be split 
between the two risk classes.

### MAR50.44 .94 defines the vega correlation between risk factors k and l as
50.44

The capital requirements for vega risk are calculated as the simple sum of vega 
capital requirements calculated independently for the following five risk classes. 
There is no vega capital requirements for counterparty credit spread risk.

### MAR50.45 .94 defines the vega correlation between risk factors k and l as
50.45

(1)
interest rate risk;
(2)
FX risk;
(3)
reference credit spread risk;
(4)
equity risk; and
(5)
commodity risk.
Delta and vega capital requirements are calculated in the same manner using the 
same procedures set out in 
 to 
.
MAR50.47
MAR50.53
50.46
For each risk class, (i) the sensitivity of the aggregate CVA,
 , and (ii) the
sensitivity of the market value of all eligible hedging instruments in the CVA
portfolio,
 , to each risk factor k in the risk class are calculated. The
sensitivities are defined as the ratio of the change of the value in question (ie (i) 
aggregate CVA or (ii) market value of all CVA hedges) caused by a small change 
of the risk factor's current value to the size of the change. Specific definitions for 
each risk class are set out in 
 to 
. These definitions include 
MAR50.54
MAR50.77
specific values of changes or shifts in risk factors. However, a bank may use 
smaller values of risk factor shifts if doing so is consistent with internal risk 
management calculations.

### MAR50.47 .94 defines the vega correlation between risk factors k and l as
50.47

FAQ
Are banks permitted under the SA-CVA to calculate CVA sensitivities 
via algorithmic techniques such as adjoint algorithmic differentiation 
(AAD)?
Yes. A bank may use AAD and similar computational techniques to 
calculate CVA sensitivities under the SA-CVA if doing so is consistent 
with the bank’s internal risk management calculations and the relevant 
validation standards described in the SA-CVA framework.
FAQ1
CVA sensitivities for vega risk are always material and must be calculated 
regardless of whether or not the portfolio includes options. When CVA 
sensitivities for vega risk are calculated, the volatility shift must apply to both 
types of volatilities that appear in exposure models:

### MAR50.48 .94 defines the vega correlation between risk factors k and l as
50.48

(1)
volatilities used for generating risk factor paths; and
(2)
volatilities used for pricing options.
If a hedging instrument is an index, its sensitivities to all risk factors upon which 
the value of the index depends must be calculated. The index sensitivity to risk 
factor k must be calculated by applying the shift of risk factor k to all index 
constituents that depend on this risk factor and recalculating the changed value 
of the index. For example, to calculate delta sensitivity of S&P500 to large 
financial companies, a bank must apply the relevant shift to equity prices of all 
large financial companies that are constituents of S&P500 and re-compute the 
index.

### MAR50.49 .94 defines the vega correlation between risk factors k and l as
50.49

For the following risk classes, a bank may choose to introduce a set of additional 
risk factors that directly correspond to qualified credit and equity indices. For 
delta risks, a credit or equity index is qualified if it satisfies liquidity and 
diversification conditions specified in 
; for vega risks, any credit or 
MAR21.31
equity index is qualified. Under this option, a bank must calculate sensitivities of 
CVA and the eligible CVA hedges to the qualified index risk factors in addition to 
sensitivities to the non-index risk factors. Under this option, for a covered 
transaction or an eligible hedging instrument whose underlying is a qualified 
index, its contribution to sensitivities to the index constituents is replaced with its 
contribution to a single sensitivity to the underlying index. For example, for a 
portfolio consisting only of equity derivatives referencing only qualified equity 
indices, no calculation of CVA sensitivities to non-index equity risk factors is 
necessary. If more than 75% of constituents of a qualified index (taking into 
account the weightings of the constituents) are mapped to the same sector, the
entire index must be mapped to that sector and treated as a single-name 
sensitivity in that bucket. In all other cases, the sensitivity must be mapped to the 
applicable index bucket.

### MAR50.50 .94 defines the vega correlation between risk factors k and l as
50.50

(1) counterparty credit spread risk;
(2) reference credit spread risk; and
(3) equity risk.
The weighted sensitivities 
 and
for each risk factor k are calculated by multiplying
the net sensitivities 
 and
, respectively, by the corresponding risk weight RW 
k
(the risk weights applicable to each risk class are specified in 
 to 
MAR50.54
MAR50.
).
77

### MAR50.51 .94 defines the vega correlation between risk factors k and l as
50.51

The net weighted sensitivity of the CVA portfolio  to risk factor k is obtained by:
sk
5
50.52
Footnotes
Note that the formula in 
 is set out under the convention 
MAR50.52
that the CVA is positive as specified in 
 (1). It intends to 
MAR50.32
recognise the risk reducing effect of hedging. For example, when 
hedging the counterparty credit spread component of CVA risk for a 
specific counterparty by buying credit protection on the counterparty: if 
the counterparty’s credit spread widens, the CVA (expressed as a 
positive value) increases resulting in the positive CVA sensitivity to the 
counterparty credit spread. At the same time, as the value of the hedge 
from the bank’s perspective increases as well (as credit protection 
becomes more valuable), the sensitivity of the hedge is also positive. 
The positive weighted sensitivities of the CVA and its hedge offset each 
other using the formula with the minus sign. If CVA loss had been 
expressed as a negative value, the minus sign in 
 would have 
MAR50.52
been replaced by a plus sign.
5
For each risk class, the net sensitivities are aggregated as follows:
50.53
(1)
The weighted sensitivities must be aggregated into a capital requirement K 
b
within each bucket b (the buckets and correlation parameters ρ applicable 
kl
to each risk class are specified in 
 to 
), where R is the 
MAR50.54
MAR50.77
hedging disallowance parameter, set at 0.01, that prevents the possibility of 
recognising perfect hedging of CVA risk.
(2)
Bucket-level capital requirements must then be aggregated across buckets 
within each risk class (the correlation parameters γbc applicable to each risk 
class are specified in 
 to 
). Note that this equation differs 
MAR50.54
MAR50.77
from the corresponding aggregation equation for market risk capital 
requirements in 
, including the multiplier m
.
MAR21.4
CVA
Interest rate buckets, risk factors, sensitivities, risk weights and correlations
(3)
In calculating K in above (2), S is defined as the sum of the weighted 
b
sensitivities WS for all risk factors k within bucket b, floored by -K and 
k
b
capped by K , and the S is defined in the same way for all risk factors k in 
b
c
bucket c:
For interest rate delta and vega risks, buckets must be set per individual 
currencies.
50.54
For interest rate delta and vega risks, cross-bucket correlation γ
 is set at 0.5 for 
bc
all currency pairs.

### MAR50.55 .94 defines the vega correlation between risk factors k and l as
50.55

The interest rate delta risk factors for a bank's reporting currency and for the 
following currencies USD, EUR, GBP, AUD, CAD, SEK or JPY:
50.56
(1)
The interest rate delta risk factors are the absolute changes of the inflation 
rate and of the risk-free yields for the following five tenors: 1 year, 2 years, 5 
years, 10 years and 30 years.
(2)
The sensitivities to the abovementioned risk-free yields are measured by 
changing the risk-free yield for a given tenor for all curves in a given 
currency by 1 basis point (0.0001 in absolute terms) and dividing the 
resulting change in the aggregate CVA (or the value of CVA hedges) by 
0.0001. The sensitivity to the inflation rate is obtained by changing the 
inflation rate by 1 basis point (0.0001 in absolute terms) and dividing the 
resulting change in the aggregate CVA (or the value of CVA hedges) by 
0.0001.
(3)
The risk weights 
 are set as follows:
RWk
Risk weight for interest rate risk (specified currencies)
Table 3
Risk factor
1 year
2 years
5 years
10 years
30 years
Inflation
Risk 
weight
1.11%
0.93%
0.74%
0.74%
0.74%
1.11%
(4)
The correlations between pairs of risk factors ρ are set as follows:
kl
Correlations for interest rate risk factors (specified currencies)
Table 4
1 year
2 years
5 years
10 
years
30 years
Inflation
1 year
100%
91%
72%
55%
31%
40%
2 years
 
100%
87%
72%
45%
40%
5 years
 
 
100%
91%
68%
40%
10 years
 
 
 
100%
83%
40%
30 years
 
 
 
 
100%
40%
Inflation
 
 
 
 
 
100%
The interest rate delta risk factors for other currencies not specified in 
:
MAR50.56
50.57
(1)
The interest rate risk factors are the absolute change of the inflation rate and 
the parallel shift of the entire risk-free yield curve for a given currency.
(2)
The sensitivity to the yield curve is measured by applying a parallel shift to all 
risk-free yield curves in a given currency by 1 basis point (0.0001 in absolute 
terms) and dividing the resulting change in the aggregate CVA (or the value 
of CVA hedges) by 0.0001. The sensitivity to the inflation rate is obtained by 
changing the inflation rate by 1 basis point (0.0001 in absolute terms) and 
dividing the resulting change in the aggregate CVA (or the value of CVA 
hedges) by 0.0001.
Foreign exchange buckets, risk factors, sensitivities, risk weights and correlations
(3)
The risk weights for both the risk-free yield curve and the inflation rate 
 
RWk
are set at 1.58%.
(4)
The correlations between the risk-free yield curve and the inflation rate ρkl 
are set at 40%.
The interest rate vega risk factors for all currencies:
50.58
(1)
The interest rate vega risk factors are a simultaneous relative change of all 
volatilities for the inflation rate and a simultaneous relative change of all 
interest rate volatilities for a given currency.
(2)
The sensitivity to (i) the interest rate volatilities or (ii) inflation rate volatilities 
is measured by respectively applying a simultaneous shift to (i) all interest 
rate volatilities or (ii) inflation rate volatilities by 1% relative to their current 
values and dividing the resulting change in the aggregate CVA (or the value 
of CVA hedges) by 0.01.
(3)
The risk weights for both the interest rate volatilities and the inflation rate 
volatilities 
 are set to 100%.
RWk
(4)
Correlations between the interest rate volatilities and the inflation rate 
volatilities ρ are set at 40%.
kl
For FX delta and vega risks, buckets must be set per individual currencies except 
for a bank’s own reporting currency.
50.59
For FX delta and vega risks, the cross-bucket correlation γ
 is set at 0.6 for all 
bc
currency pairs.

### MAR50.60 .94 defines the vega correlation between risk factors k and l as
50.60

The FX delta risk factors for all currencies:
50.61
(1)
The single FX delta risk factor is defined as the relative change of the FX spot 
rate between a given currency and a bank's reporting currency, where the FX 
spot rate is the current market price of one unit of another currency 
expressed in the units of the bank's reporting currency.
Footnotes
Counterparty credit spread buckets, risk factors, sensitivities, risk weights and 
correlations
(2)
Sensitivities to FX spot rates are measured by shifting the exchange rate 
between the bank's reporting currency and another currency (ie the value of 
one unit of another currency expressed in units of the reporting currency) by 
1% relative to its current value and dividing the resulting change in the 
aggregate CVA (or the value of CVA hedges) by 0.01. For transactions that 
reference an exchange rate between a pair of non-reporting currencies, the 
sensitivities to the FX spot rates between the bank's reporting currency and 
each of the referenced non-reporting currencies must be measured.6
(3)
The risk weights for all exchange rates between the bank's reporting 
currency and another currency are set at 11%.
For example, if a EUR-reporting bank holds an instrument that 
references the USD-GBP exchange rate, the bank must measure CVA 
sensitivity both to the EUR-GBP exchange rate and to the EUR-USD 
exchange rate.
6
The FX vega risk factors for all currencies:
50.62
(1)
The single FX vega risk factor is a simultaneous relative change of all 
volatilities for an exchange rate between a bank's reporting currency and 
another given currency.
(2)
The sensitivities to the FX volatilities are measured by simultaneously shifting 
all volatilities for a given exchange rate between the bank's reporting 
currency and another currency by 1% relative to their current values and 
dividing the resulting change in the aggregate CVA (or the value of CVA 
hedges) by 0.01. For transactions that reference an exchange rate between a 
pair of non-reporting currencies, the volatilities of the FX spot rates between 
the bank's reporting currency and each of the referenced non-reporting 
currencies must be measured.
(3)
The risk weights for FX volatilities 
 are set to 100%.
RWk
Counterparty credit spread risk is not subject to vega risk capital requirements. 
Buckets for delta risk are set as follows:
50.63
(1)
Buckets 1 to 7 are defined for factors that are not qualified indices as set out 
in 
;
MAR50.50
(2)
Bucket 8 is set for the optional treatment of qualified indices. Under the 
optional treatment, only instruments that reference qualified indices can be 
assigned to bucket 8, while all single-name and all non-qualified index 
hedges must be assigned to buckets 1 to 7 for calculations of CVA 
sensitivities and sensitivities. For any instrument referencing an index 
assigned to buckets 1 to 7, the look-through approach must be used (ie, 
sensitivity of the hedge to each index constituent must be calculated).
Buckets for counterparty credit spread delta risk
Table 5
Bucket number
Sector
1
a) Sovereigns including central banks, multilateral development banks
b) Local government, government-backed non-financials, education and 
public administration
2
Financials including government-backed financials
3
Basic materials, energy, industrials, agriculture, manufacturing, mining 
and quarrying
4
Consumer goods and services, transportation and storage, administrative 
and support service activities
5
Technology, telecommunications
6
Health care, utilities, professional and technical activities
7
Other sector
8
Qualified Indices
For counterparty credit spread delta risk, the cross-bucket correlations γ
 are set 
bc
as follows:

### MAR50.64 .94 defines the vega correlation between risk factors k and l as
50.64

Cross-bucket correlations for counterparty credit spread delta risk
Table 6
Bucket
1
2
3
4
5
6
7
8
1
100%
10%
20%
25%
20%
15%
0%
45%
2
100%
5%
15%
20%
5%
0%
45%
3
 
 
100%
20%
25%
5%
0%
45%
4
 
 
 
100%
25%
5%
0%
45%
5
 
 
 
 
100%
5%
0%
45%
6
 
 
 
 
 
100%
0%
45%
7
 
 
 
 
 
 
100%
0%
8
 
 
 
 
 
 
 
100%
The counterparty credit spread delta risk factors for a given bucket:
50.65
(1)
The counterparty credit spread delta risk factors are absolute shifts of credit 
spreads of individual entities (counterparties and reference names for 
counterparty credit spread hedges) and qualified indices (if the optional 
treatment is chosen) for the following tenors: 0.5 years, 1 year, 3 years, 5 
years and 10 years.
(2)
For each entity and each tenor point, the sensitivities are measured by 
shifting the relevant credit spread by 1 basis point (0.0001 in absolute terms) 
and dividing the resulting change in the aggregate CVA (or the value of CVA 
hedges) by 0.0001.
(3)
The risk weights 
 are set as follows depending on the entity's bucket, 
RWk
where IG, HY and NR represent "investment grade", "high yield" and "not 
rated" as specified for the BA-CVA in 
. The same risk weight for a 
MAR50.16
given bucket and given credit quality applies to all tenors.
Risk weights for counterparty credit spread delta risk
Table
7
Bucket
1 a)
1 b)
2
3
4
5
6
7
8
IG names
0.5%
1.0%
5.0%
3.0%
3.0%
2.0%
1.5%
5.0%
1.5%
HY and 
NR names
2.0%
4.0%
12.0%
7.0%
8.5%
5.5%
5.0%
12.0%
5.0%
(4)
For buckets 1 to 7, the correlation parameter ρ between two weighted 
kl
sensitivities WS and WS is calculated as follows, where:
k
l
(a)
ρ
 is equal to 100% if the two tenors are the same and 90% 
tenor
otherwise;
(b)
ρ
 is equal to 100% if the two names are the same, 90% if the two 
name
names are distinct, but legally related and 50% otherwise;
(c)
ρ
 is equal to 100% if the credit quality of the two names is the 
quality
same (ie IG and IG or HY/NR and HY/NR) and 80% otherwise.
Reference credit spread buckets, risk factors, sensitivities, risk weights and 
correlations
(5)
For bucket 8, the correlation parameter ρ between two weighted 
kl
sensitivities WS and WS is calculated as follows, where:
k
l
(a)
ρ
 is equal to 100% if the two tenors are the same and 90% 
tenor
otherwise;
(b)
ρname is equal to 100% if the two indices are the same and of the same
series, 90% if the two indices are the same, but of distinct series, and 
80% otherwise;
(c)
ρ
 is equal to 100% if the credit quality of the two indices is the 
quality
same (ie IG and IG or HY and HY) and 80% otherwise.
Reference credit spread risk is subject to both delta and vega risk capital 
requirements. Buckets for delta and vega risks are set as follows, where IG, HY 
and NR represent "investment grade", "high yield" and "not rated" as specified 
for the BA-CVA in 
:
MAR50.16

### MAR50.66 .94 defines the vega correlation between risk factors k and l as
50.66

Buckets for reference credit spread risk
Table 8
Bucket 
number
Credit quality
Sector
1
IG
Sovereigns including central banks, multilateral 
development banks
2
Local government, government-backed non-financials, 
education and public administration
3
Financials including government-backed financials
4
Basic materials, energy, industrials, agriculture, 
manufacturing, mining and quarrying
5
Consumer goods and services, transportation and storage, 
administrative and support service activities
6
Technology, telecommunications
7
Health care, utilities, professional and technical activities
8
HY and NR
Sovereigns including central banks, multilateral 
development banks
9
Local government, government-backed non-financials, 
education and public administration
10
Financials including government-backed financials
11
Basic materials, energy, industrials, agriculture, 
manufacturing, mining and quarrying
12
Consumer goods and services, transportation and storage, 
administrative and support service activities
13
Technology, telecommunications
14
Health care, utilities, professional and technical activities
15
(Not 
applicable)
Other sector
16
IG
Qualified Indices
17
HY
Qualified Indices
For reference credit spread delta and vega risks, the cross-bucket correlations γ
 
bc
are set as follows:

### MAR50.67 .94 defines the vega correlation between risk factors k and l as
50.67

(1)
The cross-bucket correlations γ
 between buckets of the same credit quality 
bc
(ie either IG or HY/NR) are set as follows:
Cross-bucket correlations for reference credit spread risk
Table
9
Bucket
1/8
2/9
3/10
4/11
5/12
6/13
7/14
15
16
17
15
 
 
 
 
 
 
 
100%
0%
0%
16
 
 
 
 
 
 
 
 
100%
75%
17
 
 
 
 
 
 
 
 
 
100%
(2)
For cross-bucket correlations γ
 between buckets 1 to 14 of different credit 
bc
quality (ie IG and HY/NR), the correlations γ
 specified in 
(1) are 
bc
MAR50.67
divided by 2.
Reference credit spread delta risk factors for a given bucket:
50.68
(1)
The single reference credit spread delta risk factor is a simultaneous absolute 
shift of the credit spreads of all tenors for all reference names in the bucket.
Equity buckets, risk factors, sensitivities, risk weights and correlations
(2)
The sensitivity to reference credit spread delta risk is measured by 
simultaneously shifting the credit spreads of all tenors for all reference
names in the bucket by 1 basis point (0.0001 in absolute terms) and dividing 
the resulting change in the aggregate CVA (or the value of CVA hedges) by 
0.0001.
(3)
The risk weights 
 are set as follows depending on the reference name's 
RWk
bucket:
Risk weights for reference credit spread delta risk
Table 10
IG bucket
1
2
3
4
5
6
7
8
9
Risk weight
0.5%
1.0%
5.0%
3.0%
3.0%
2.0%
1.5%
2.0%
4.0%
HY/NR bucket
10
11
12
13
14
15
16
17
Risk weight
12.0%
7.0%
8.5%
5.5%
5.0%
12.0%
1.5%
5.0%
Reference credit spread vega risk factors for a given bucket:
50.69
(1)
The single reference credit spread vega risk factor is a simultaneous relative 
shift of the volatilities of credit spreads of all tenors for all reference names 
in the bucket.
(2)
The sensitivity to the reference credit spread vega risk factor is measured by 
simultaneously shifting the volatilities of credit spreads of all tenors for all 
reference names in the bucket by 1% relative to their current values and 
dividing the resulting change in the aggregate CVA (or the value of CVA 
hedges) by 0.01.
(3)
Risk weights for reference credit spread volatilities 
 are set to 100%.
RWk
For equity delta and vega risks, buckets are set as follows, where:
50.70
(1)
Market capitalisation ("market cap") is defined as the sum of the market 
capitalisations of the same legal entity or group of legal entities across all 
stock markets globally. The reference to "group of legal entities" covers 
cases where the listed entity is a parent company of a group of legal entities.
Under no circumstances should the sum of the market capitalisations of 
multiple related listed entities be used to determine whether a listed entity is 
"large market cap" or "small market cap".
(2)
"Large market cap" is defined as a market capitalisation equal to or greater 
than USD 2 billion and "small market cap" is defined as a market 
capitalisation of less than USD 2 billion.
(3)
The advanced economies are Canada, the United States, Mexico, the euro 
area, the non-euro area western European countries (the United Kingdom, 
Norway, Sweden, Denmark and Switzerland), Japan, Oceania (Australia and 
New Zealand), Singapore and Hong Kong SAR.
(4)
To assign a risk exposure to a sector, banks must rely on a classification that 
is commonly used in the market for grouping issuers by industry sector. The 
bank must assign each issuer to one of the sector buckets in the table above 
and it must assign all issuers from the same industry to the same sector. Risk 
positions from any issuer that a bank cannot assign to a sector in this fashion 
must be assigned to the "other sector" (ie bucket 11). For multinational multi-
sector equity issuers, the allocation to a particular bucket must be done 
according to the most material region and sector in which the issuer 
operates.
Buckets for equity risk
Table 11
Bucket 
number
Size
Region
Sector
1
Large
Emerging 
market 
economies
Consumer goods and services, transportation and 
storage, administrative and support service activities, 
healthcare, utilities
2
Telecommunications, industrials
3
Basic materials, energy, agriculture, manufacturing, 
mining and quarrying
4
Financials including government-backed financials, 
real estate activities, technology
5
Advanced 
economies
Consumer goods and services, transportation and 
storage, administrative and support service activities, 
healthcare, utilities
6
Telecommunications, industrials
7
Basic materials, energy, agriculture, manufacturing, 
mining and quarrying
8
Financials including government-backed financials, 
real estate activities, technology
9
Small
Emerging 
market 
economies
All sectors described under bucket numbers 1, 2, 3, 
and 4
10
Advanced 
economies
All sectors described under bucket numbers 5, 6, 7, 
and 8
11
(Not applicable)
Other sector
12
Qualified Indices
Large cap, 
advanced 
economies
13
Other
Qualified Indices
For equity delta and vega risks, cross-bucket correlation γ
 is set at 15% for all 
bc
cross-bucket pairs that fall within bucket numbers 1 to 10. The cross-bucket 
correlation between buckets 12 and 13 is set at 75% and the cross bucket 
correlation between buckets 12 or 13 and any of the buckets 1 to 10 is 45%. γ
 is 
bc
set at 0% for all cross-bucket pairs that include bucket 11.

### MAR50.71 .94 defines the vega correlation between risk factors k and l as
50.71

Equity delta risk factors for a given bucket:
50.72
(1)
The single equity delta risk factor is a simultaneous relative shift of equity 
spot prices for all reference names in the bucket.
(2)
The sensitivity to the equity delta risk factor is measured by simultaneously 
shifting the equity spot prices for all reference names in the bucket by 1% 
relative to their current values and dividing the resulting change in the 
aggregate CVA (or the value of CVA hedges) by 0.01.
(3)
Risk weights 
 are set as follows depending on the reference name's 
RWk
bucket:
Risk weights for equity delta risk
Table 12
Bucket number
Risk weight
1
55%
2
60%
3
45%
4
55%
5
30%
6
35%
7
40%
8
50%
9
70%
10
50%
11
70%
12
15%
13
25%
Equity vega risk factors for a given bucket:
50.73
(1)
The single equity vega risk factor is a simultaneous relative shift of the 
volatilities for all reference names in the bucket.
(2)
The sensitivity to the equity vega risk factor is measured by simultaneously 
shifting the volatilities for all reference names in the bucket by 1% relative to 
their current values and dividing the resulting change in the aggregate CVA 
(or the value of CVA hedges) by 0.01.
Commodity buckets, risk factors, sensitivities, risk weights and correlations
(3)
The risk weights for equity volatilities 
 are set to 78% for large market 
RWk
capitalisation buckets and to 100% for the other buckets.
For commodity delta and vega risks, buckets are set as follows:
50.74
Buckets for commodity risk
Table 13
Bucket 
number
Commodity group
Examples
1
Energy – Solid
combustibles
coal, charcoal, wood pellets, nuclear fuel (such as
uranium)
2
Energy – Liquid
combustibles
crude oil (such as Light-sweet, heavy, West Texas
Intermediate and Brent); biofuels (such as 
bioethanol and biodiesel); petrochemicals (such
as propane, ethane, gasoline, methanol and 
butane); refined fuels (such as jet fuel, kerosene,
gasoil, fuel oil, naphtha, heating oil and diesel)
3
Energy – Electricity and
carbon trading
electricity (such as spot, day-ahead, peak and off-
peak); carbon emissions trading (such as certified
emissions reductions, in-delivery month EU 
allowance, Regional Greenhouse Gas Initiative 
CO2 allowance and renewable energy certificates)
4
Freight
dry-bulk route (such as Capesize, Panamax,
Handysize and Supramax); liquid-bulk/gas 
shipping route (such as Suezmax, Aframax and
very large crude carriers)
5
Metals – non-precious
base metal (such as aluminium, copper, lead, 
nickel, tin and zinc); steel raw materials (such as
steel billet, steel wire, steel coil, steel scrap and 
steel rebar, iron ore, tungsten, vanadium, titanium
and tantalum); minor metals (such as cobalt,
manganese, molybdenum)
6
Gaseous combustibles
natural gas; liquefied natural gas
7
Precious metals
(including gold)
gold; silver; platinum; palladium
8
Grains & oilseed
corn; wheat; soybean (such as soybean seed, 
soybean oil and soybean meal); oats; palm oil; 
canola; barley; rapeseed (such as rapeseed seed,
rapeseed oil, and rapeseed meal); red bean,
sorghum; coconut oil; olive oil; peanut oil;
sunflower oil; rice
9
Livestock & dairy
cattle (such live and feeder); hog; poultry; lamb;
fish; shrimp; dairy (such as milk, whey, eggs,
butter and cheese)
10
Softs and other
agriculturals
cocoa; coffee (such as arabica and robusta); tea; 
citrus and orange juice; potatoes; sugar; cotton;
wool; lumber and pulp; rubber
11
Other commodity
industrial minerals (such as potash, fertiliser and
phosphate rocks), rare earths; terephthalic acid;
flat glass
For commodity delta and vega risks, cross-bucket correlation γ
 is set at 20% for 
bc
all cross-bucket pairs that fall within bucket numbers 1 to 10. γ
 is set at 0% for 
bc
all cross-bucket pairs that include bucket 11.

### MAR50.75 .94 defines the vega correlation between risk factors k and l as
50.75

Commodity delta risk factors for a given bucket:
50.76
(1)
The single commodity delta risk factor is a simultaneous relative shift of the 
commodity spot prices for all commodities in the bucket.
(2)
The sensitivities to commodity delta risk factors are measured by 
simultaneously shifting the spot prices of all commodities in the bucket by 
1% relative to their current values and dividing the resulting change in the 
aggregate CVA (or the value of CVA hedges) by 0.01.
(3)
The risk weights 
 are set as follows depending on the reference name's 
RWk
bucket:
Risk weights for commodity delta risk
Table 14
Bucket 
number
1
2
3
4
5
6
7
8
9
10
11
RW
30%
35%
60%
80%
40%
45%
20%
35%
25%
35%
50%
Commodity vega risk factors for a given bucket:
50.77
(1)
The single commodity vega risk factor is a simultaneous relative shift of the 
volatilities for all commodities in the bucket.
(2)
The sensitivity to the commodity vega risk factor is measured by 
simultaneously shifting the volatilities for all commodities in the bucket by 
1% relative to their current values and dividing the resulting change in the 
aggregate CVA (or the value of CVA hedges) by 0.01.
(3)
The risk weights for commodity volatilities 
 are set to 100%. 
RWk

## MAR90 .94 defines the vega correlation between risk factors k and l as

Transitional arrangements
This chapter sets out transitional arrangements 
for the Pillar 1 consequences of the outcomes of 
the P&L attribution test that apply until 1 
January 2023.
Version effective as of
01 Jan 2023
Banks are required to conduct the profit and loss (P&L) attribution (PLA) test 
beginning 1 January 2023 as set out in 
. The outcomes of the PLA test 
MAR32.3
will be used for Pillar 2 purposes beginning 1 January 2023. The Pillar 1 capital 
requirement consequences of assignment to the PLA test amber zone or PLA test 
red zone, as set out in 
, 
 and 
, will apply beginning 
MAR32.43 MAR32.44
MAR33.43
1 January 2024.

### MAR90.1 .94 defines the vega correlation between risk factors k and l as
90.1


## MAR99 .94 defines the vega correlation between risk factors k and l as

Guidance on use of the 
internal models approach
This chapter sets out application guidance for 
backtesting requirements and principles for risk 
factor modellability under the internal models 
approach for market risk capital requirements.
Version effective as of
01 Jan 2023
Reflects revisions to internal models approach 
and updated to take account of the revised 
implementation date announced on 27 March 
2020.
Trading desk-level backtesting
An additional consideration in specifying the appropriate risk measures and 
trading outcomes for profit and loss (P&L) attribution test and backtesting arises 
because the internally modelled risk measurement is generally based on the 
sensitivity of a static portfolio to instantaneous price shocks. That is, end-of-day 
trading positions are input into the risk measurement model, which assesses the 
possible change in the value of this static portfolio due to price and rate 
movements over the assumed holding period.

### MAR99.1 .94 defines the vega correlation between risk factors k and l as
99.1

While this is straightforward in theory, in practice it complicates the issue of 
backtesting. For instance, it is often argued that neither expected shortfall nor 
value-at-risk measures can be compared against actual trading outcomes, since 
the actual outcomes will reflect changes in portfolio composition during the 
holding period. According to this view, the inclusion of fee income together with 
trading gains and losses resulting from changes in the composition of the 
portfolio should not be included in the definition of the trading outcome because 
they do not relate to the risk inherent in the static portfolio that was assumed in 
constructing the value-at-risk measure.

### MAR99.2 .94 defines the vega correlation between risk factors k and l as
99.2

This argument is persuasive with regard to the use of risk measures based on 
price shocks calibrated to longer holding periods. That is, comparing the liquidity-
adjusted time horizon 99th percentile risk measures from the internal models 
capital requirement with actual liquidity-adjusted time horizon trading outcomes 
would probably not be a meaningful exercise. In particular, in any given multi-day 
period, significant changes in portfolio composition relative to the initial positions 
are common at major trading institutions. For this reason, the backtesting 
framework described here involves the use of risk measures calibrated to a one-
day holding period. Other than the restrictions mentioned in this paper, the test 
would be based on how banks model risk internally.

### MAR99.3 .94 defines the vega correlation between risk factors k and l as
99.3

Given the use of one-day risk measures, it is appropriate to employ one-day 
trading outcomes as the benchmark to use in the backtesting programme. The 
same concerns about “contamination” of the trading outcomes discussed above 
continue to be relevant, however, even for one-day trading outcomes. That is, 
there is a concern that the overall one-day trading outcome is not a suitable 
point of comparison, because it reflects the effects of intraday trading, possibly 
including fee income that is booked in connection with the sale of new products.

### MAR99.4 .94 defines the vega correlation between risk factors k and l as
99.4

Bank-wide backtesting
On the one hand, intraday trading will tend to increase the volatility of trading 
outcomes and may result in cases where the overall trading outcome exceeds the 
risk measure. This event clearly does not imply a problem with the methods used 
to calculate the risk measure; rather, it is simply outside the scope of what the 
measure is intended to capture. On the other hand, including fee income may
similarly distort the backtest, but in the other direction, since fee income often 
has annuity-like characteristics. Since this fee income is not typically included in 
the calculation of the risk measure, problems with the risk measurement model 
could be masked by including fee income in the definition of the trading 
outcome used for backtesting purposes.

### MAR99.5 .94 defines the vega correlation between risk factors k and l as
99.5

To the extent that backtesting programmes are viewed purely as a statistical test 
of the integrity of the calculation of the risk measures, it is appropriate to employ 
a definition of daily trading outcome that allows for an uncontaminated test. To 
meet this standard, banks must have the capability to perform the tests based on 
the hypothetical changes in portfolio value that would occur were end-of-day 
positions to remain unchanged.

### MAR99.6 .94 defines the vega correlation between risk factors k and l as
99.6

Backtesting using actual daily P&Ls is also a useful exercise since it can uncover 
cases where the risk measures are not accurately capturing trading volatility in 
spite of being calculated with integrity.

### MAR99.7 .94 defines the vega correlation between risk factors k and l as
99.7

For these reasons, the Committee requires banks to develop the capability to 
perform these tests using both hypothetical and actual trading outcomes. In 
combination, the two approaches are likely to provide a strong understanding of 
the relation between calculated risk measures and trading outcomes. The total 
number of backtesting exceptions for the purpose of the thresholds in 
 
MAR32.9
must be calculated as the maximum of the exceptions generated under 
hypothetical or actual trading outcomes.

### MAR99.8 .94 defines the vega correlation between risk factors k and l as
99.8

To place the definitions of three zones of the bank-wide backtesting in proper 
perspective, however, it is useful to examine the probabilities of obtaining various 
numbers of exceptions under different assumptions about the accuracy of a bank’
s risk measurement model.

### MAR99.9 .94 defines the vega correlation between risk factors k and l as
99.9

Three zones have been delineated and their boundaries chosen in order to 
balance two types of statistical error: 
99.10
(1)
the possibility that an accurate risk model would be classified as inaccurate 
on the basis of its backtesting result, and
(2)
the possibility that an inaccurate model would not be classified that way 
based on its backtesting result.
Table 1 reports the probabilities of obtaining a particular number of exceptions 
from a sample of 250 independent observations under several assumptions about 
the actual percentage of outcomes that the model captures (ie these are binomial 
probabilities). For example, the left-hand portion of Table 1 sets out probabilities 
associated with an accurate model (that is, a true coverage level of 99%). Under 
these assumptions, the column labelled “exact” reports that exactly five 
exceptions can be expected in 6.7% of the samples.

### MAR99.11 .94 defines the vega correlation between risk factors k and l as
99.11

Probabilities of exceptions from 250 independent observations
Table 1
Model is accurate
Model is inaccurate: possible alternative levels of coverage
Coverage = 99% Coverage = 98% Coverage = 97% Coverage = 96% Coverage = 95%
Exact
Type 1
Exact
Type 2
Exact
Type 2
Exact
Type 2
Exact
Type 2
0
8.1%
100.0%
0.6%
0.0%
0.0%
0.0%
0.0%
0.0%
0.0%
0.0%
1
20.5%
91.9%
3.3%
0.6%
0.4%
0.0%
0.0%
0.0%
0.0%
0.0%
2
25.7%
71.4%
8.3%
3.9%
1.5%
0.4%
0.2%
0.0%
0.0%
0.0%
3
21.5%
45.7%
14.0%
12.2%
3.8%
1.9%
0.7%
0.2%
0.1%
0.0%
4
13.4%
24.2%
17.7%
26.2%
7.2%
5.7%
1.8%
0.9%
0.3%
0.1%
5
6.7%
10.8%
17.7%
43.9%
10.9%
12.8%
3.6%
2.7%
0.9%
0.5%
6
2.7%
4.1%
14.8%
61.6%
13.8%
23.7%
6.2%
6.3%
1.8%
1.3%
7
1.0%
1.4%
10.5%
76.4%
14.9%
37.5%
9.0%
12.5%
3.4%
3.1%
8
0.3%
0.4%
6.5%
86.9%
14.0%
52.4%
11.3%
21.5%
5.4%
6.5%
9
0.1%
0.1%
3.6%
93.4%
11.6%
66.3%
12.7%
32.8%
7.6%
11.9%
10
0.0%
0.0%
1.8%
97.0%
8.6%
77.9%
12.8%
45.5%
9.6%
19.5%
11
0.0%
0.0%
0.8%
98.7%
5.8%
86.6%
11.6%
58.3%
11.1%
29.1%
12
0.0%
0.0%
0.3%
99.5%
3.6%
92.4%
9.6%
69.9%
11.6%
40.2%
13
0.0%
0.0%
0.1%
99.8%
2.0%
96.0%
7.3%
79.5%
11.2%
51.8%
14
0.0%
0.0%
0.0%
99.9%
1.1%
98.0%
5.2%
86.9%
10.0%
62.9%
15
0.0%
0.0%
0.0%
100.0%
0.5%
99.1%
3.4%
92.1%
8.2%
72.9%
Notes to Table 1: The table reports both exact probabilities of obtaining a certain number of
exceptions from a sample of 250 independent observations under several assumptions about
the true level of coverage, as well as type 1 or type 2 error probabilities derived from these
exact probabilities.
The left-hand portion of the table pertains to the case where the model is accurate and its
true level of coverage is 99%. Thus, the probability of any given observation being an
exception is 1% (100% – 99% = 1%). The column labelled "exact" reports the probability of
obtaining exactly the number of exceptions shown under this assumption in a sample of 250
independent observations. The column labelled "type 1" reports the probability that using a
given number of exceptions as the cut-off for rejecting a model will imply erroneous rejection
of an accurate model using a sample of 250 independent observations. For example, if the
cut-off level is set at five or more exceptions, the type 1 column reports the probability of
falsely rejecting an accurate model with 250 independent observations is 10.8%.
The right-hand portion of the table pertains to models that are inaccurate. In particular, the
table concentrates of four specific inaccurate models, namely models whose true levels of
coverage are 98%, 97%, 96% and 95% respectively. For each inaccurate model, the exact
column reports the probability of obtaining exactly the number of exceptions shown under
this assumption in a sample of 250 independent observations. The type 2 columns report the
probability that using a given number of exceptions as the cut-off for rejecting a model will
imply erroneous acceptance of an inaccurate model with the assumed level of coverage using
a sample of 250 independent observations. For example, if the cut-off level is set at five or
more exceptions, the type 2 column for an assumed coverage level of 97% reports the
probability of falsely accepting a model with only 97% coverage with 250 independent
observations is 12.8%.
The right-hand portion of the table reports probabilities associated with several 
possible inaccurate models, namely models whose true levels of coverage are 
98%, 97%, 96%, and 95%, respectively. Thus, the column labelled “exact” under an 
assumed coverage level of 97% shows that five exceptions would then be 
expected in 10.9% of the samples.

### MAR99.12 .94 defines the vega correlation between risk factors k and l as
99.12

Table 1 also reports several important error probabilities. For the assumption that 
the model covers 99% of outcomes (the desired level of coverage), the table 
reports the probability that selecting a given number of exceptions as a threshold 
for rejecting the accuracy of the model will result in an erroneous rejection of an 
accurate model (type 1 error). For example, if the threshold is set as low as one 
exception, then accurate models will be rejected fully 91.9% of the time, because 
they will escape rejection only in the 8.1% of cases where they generate zero 
exceptions. As the threshold number of exceptions is increased, the probability of 
making this type of error declines.

### MAR99.13 .94 defines the vega correlation between risk factors k and l as
99.13

Under the assumptions that the model’s true level of coverage is not 99%, the 
table reports the probability that selecting a given number of exceptions as a 
threshold for rejecting the accuracy of the model will result in an erroneous 
acceptance of a model with the assumed (inaccurate) level of coverage (type 2 
error). For example, if the model’s actual level of coverage is 97%, and the 
threshold for rejection is set at seven or more exceptions, the table indicates that 
this model would be erroneously accepted 37.5% of the time.

### MAR99.14 .94 defines the vega correlation between risk factors k and l as
99.14

The results in Table 1 also demonstrate some of the statistical limitations of 
backtesting. In particular, there is no threshold number of exceptions that yields
both a low probability of erroneously rejecting an accurate model and a low 
probability of erroneously accepting all of the relevant inaccurate models. It is for 
this reason that the Committee has rejected an approach that contains only a 
single threshold.

### MAR99.15 .94 defines the vega correlation between risk factors k and l as
99.15

Given these limitations, the Committee has classified outcomes for the 
backtesting of the bank-wide model into three categories. In the first category, 
the test results are consistent with an accurate model, and the possibility of 
erroneously accepting an inaccurate model is low (ie backtesting ”green zone”). 
At the other extreme, the test results are extremely unlikely to have resulted from 
an accurate model, and the probability of erroneously rejecting an accurate 
model on this basis is remote (ie backtesting ”red zone”). In between these two 
cases, however, is a zone where the backtesting results could be consistent with 
either accurate or inaccurate models, and the supervisor should encourage a 
bank to present additional information about its model before taking action (ie 
backtesting ”amber zone”).

### MAR99.16 .94 defines the vega correlation between risk factors k and l as
99.16

Table 2 sets out the Committee’s agreed boundaries for these zones and the 
presumptive supervisory response for each backtesting outcome, based on a 
sample of 250 observations. For other sample sizes, the boundaries should be 
deduced by calculating the binomial probabilities associated with true coverage 
of 99%, as in Table 1. The backtesting amber zone begins at the point such that 
the probability of obtaining that number or fewer exceptions equals or exceeds 
95%. Table 2 reports these cumulative probabilities for each number of 
exceptions. For 250 observations, it can be seen that five or fewer exceptions will 
be obtained 95.88% of the time when the true level of coverage is 99%. Thus, the 
backtesting amber zone begins at five exceptions. Similarly, the beginning of the 
backtesting red zone is defined as the point such that the probability of obtaining 
that number or fewer exceptions equals or exceeds 99.99%. Table 2 shows that 
for a sample of 250 observations and a true coverage level of 99%, this occurs 
with 10 exceptions.

### MAR99.17 .94 defines the vega correlation between risk factors k and l as
99.17

Backtesting zone boundaries
Table 2
Backtesting zone
Number of
exceptions
Backtesting-dependent
multiplier
(to be added to any 
qualitative add-on per
)
MAR33.44
Cumulative probability
Green
0
1
2
3
4
1.50
1.50
1.50
1.50
1.50
8.11%
28.58%
54.32%
75.81%
89.22%
Amber
5
6
7
8
9
1.70
1.76
1.83
1.88
1.92
95.88%
98.63%

### MAR99.60 %
99.60%


### MAR99.89 %
99.89%


### MAR99.97 %
99.97%

Red
10 or more
2.00
99.99%
Notes to Table 2: The table defines the backtesting green, amber and red zones that
supervisors will use to assess backtesting results in conjunction with the internal models
approach to market risk capital requirements. The boundaries shown in the table are based
on a sample of 250 observations. For other sample sizes, the amber zone begins at the point
where the cumulative probability equals or exceeds 95%, and the red zone begins at the
point where the cumulative probability equals or exceeds 99.99%.
The cumulative probability is simply the probability of obtaining a given number or fewer
exceptions in a sample of 250 observations when the true coverage level is 99%. For example,
the cumulative probability shown for four exceptions is the probability of obtaining between
zero and four exceptions.
Note that these cumulative probabilities and the type 1 error probabilities reported in Table 1
do not sum to one because the cumulative probability for a given number of exceptions
includes the possibility of obtaining exactly that number of exceptions, as does the type 1
error probability. Thus, the sum of these two probabilities exceeds one by the amount of the
probability of obtaining exactly that number of exceptions.
Examples of the application of the principles for risk factor 
modellability
The backtesting green zone needs little explanation. Since a model that truly 
provides 99% coverage would be quite likely to produce as many as four 
exceptions in a sample of 250 outcomes, there is little reason for concern raised 
by backtesting results that fall in this range. This is reinforced by the results in 
Table 1, which indicate that accepting outcomes in this range leads to only a 
small chance of erroneously accepting an inaccurate model.

### MAR99.18 .94 defines the vega correlation between risk factors k and l as
99.18

The range from five to nine exceptions constitutes the backtesting amber zone. 
Outcomes in this range are plausible for both accurate and inaccurate models, 
although Table 1 suggests that they are generally more likely for inaccurate 
models than for accurate models. Moreover, the results in Table 1 indicate that 
the presumption that the model is inaccurate should grow as the number of 
exceptions increases in the range from five to nine.

### MAR99.19 .94 defines the vega correlation between risk factors k and l as
99.19

Table 2 sets out the Committee’s agreed guidelines for increases in the 
multiplication factor applicable to the internal models capital requirement, 
resulting from backtesting results in the backtesting amber zone.

### MAR99.20 .94 defines the vega correlation between risk factors k and l as
99.20

These particular values reflect the general idea that the increase in the 
multiplication factor should be sufficient to return the model to a 99th percentile 
standard. For example, five exceptions in a sample of 250 imply only 98% 
coverage. Thus, the increase in the multiplication factor should be sufficient to 
transform a model with 98% coverage into one with 99% coverage. Needless to 
say, precise calculations of this sort require additional statistical assumptions that 
are not likely to hold in all cases. For example, if the distribution of trading 
outcomes is assumed to be normal, then the ratio of the 99th percentile to the 
98th percentile is approximately 1.14, and the increase needed in the 
multiplication factor is therefore approximately 1.13 for a multiplier of 1. If the 
actual distribution is not normal, but instead has “fat tails”, then larger increases 
may be required to reach the 99th percentile standard. The concern about fat 
tails was also an important factor in the choice of the specific increments set out 
in Table 2.

### MAR99.21 .94 defines the vega correlation between risk factors k and l as
99.21

Although supervisors may use discretion regarding the types of evidence 
required of banks to provide risk factor modellability, the following are examples 
of the types of evidence that banks may be required to provide.

### MAR99.22 .94 defines the vega correlation between risk factors k and l as
99.22

(1)
Regression diagnostics for multi-factor beta models. In addition to showing 
that indices or other regressors are appropriate for the region, asset class 
and credit quality (if applicable) of an instrument, banks must be prepared to 
demonstrate that the coefficients used in multi-factor models are adequate
to capture both general market risk and idiosyncratic risk. If the bank 
assumes that the residuals from the multi-factor model are uncorrelated with 
each other, the bank should be prepared to demonstrate that the modellable 
residuals are uncorrelated. Further, the factors in the multi-factor model 
must be appropriate for the region and asset class of the instrument and 
must explain the general market risk of the instrument. This must be 
demonstrated through goodness-of-fit statistics (eg an adjusted-R2 
coefficient) and other diagnostics on the coefficients. Most importantly, 
where the estimated coefficients are not used (ie the parameters are 
judgment-based), the bank must describe how the coefficients are chosen 
and why they cannot be estimated, and demonstrate that the choice does 
not underestimate risk. In general, risk factors are not considered modellable 
in cases where parameters are set by judgment.
(2)
Recovery of price from risk factors. The bank must periodically demonstrate 
and document that the risk factors used in its risk model can be fed into 
front office pricing models and recover the actual prices of the assets. If the 
recovered prices substantially deviate from the actual prices, this can indicate 
a problem with prices used to derive the risk factors and call into question 
the validity of data inputs for risk purposes. In such cases, supervisors may 
determine that the risk factor is non-modellable.
(3)
Risk pricing is periodically reconciled with front office and back office prices. 
While banks are free to use price data from external sources, these external 
prices should periodically be reconciled with internal prices (from both front 
office and back office) to ensure they do not deviate substantially, and that 
they are not consistently biased in any fashion. Results of these 
reconciliations should be made available to supervisors, including statistics 
on the differences of the risk price from front office and back office prices. It 
is standard practice for banks to conduct reconciliation of front office and 
back office prices; the risk prices must be included as part of the 
reconciliation of the front office and whenever there is a potential for 
discrepancy. If the discrepancy is large, supervisors may determine that the 
risk factor is non-modellable.
(4)
Risk factor backtesting. Banks must periodically demonstrate the 
appropriateness of their modelling methodology by comparing the risk 
factor returns forecast produced by the risk management model with actual 
returns produced by front office prices. Alternatively, a bank could backtest 
hypothetical portfolios that are substantively dependent on key risk factors
(or combinations thereof). This risk factor backtesting is intended to confirm 
that risk factors accurately reflect the volatility and correlations of the 
instruments in the risk model. Hypothetical backtesting can be effective in 
identifying whether risk factors in question adequately reflect volatility and 
correlations when the portfolio of instruments is chosen to highlight specific 
products.
(5)
Risk factors generated from parameterised models. For options, implied 
volatility surfaces are often built using a parameterised model based on 
single-name underlyings and/or option index RPOs and/or market quotes. 
Liquid options at moneyness, tenor and option expiry points may be used to 
calibrate level, volatility, drift and correlation parameters for a single-name 
or benchmark volatility surface. Once these parameters are set, they are 
derived risk factors in their own right that must be updated and recalibrated 
periodically as new data arrive and trades occur. In the event that these risk 
factors are used to proxy for other single-name option surface points, there 
must be an additional-basis non-modellable risk factor overlay for any 
potential deviations.
OPE
Calculation of RWA for 
operational risk
This standard describes how to calculate capital 
requirements for operational risk.