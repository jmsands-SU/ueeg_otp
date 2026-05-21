# --- Variable Definitions ---

# PMU
PMU_BGR_RSEL_3_0 = 0b1000
# offset = 0b000 # Commented out in original C code
PMU_IBN_ENB_12_0 = 0b0000111111011
PMU_VDDA_SELB_2_0 = 0b111
PMU_VDDVCO_SELB_3_0 = 0b1100
PMU_POR_SEL_2_0 = 0b000
PMU_VDDD_SELB_2_0 = 0b100
PMU_VDDADC_SEL_2_0 = 0b111
PMU_VPA_SEL_2_0 = 0b111
PMU_REFSEL_CM_2_0 = 0b010
PMU_REFSEL_HI_3_0 = 0b0010
PMU_REFSEL_LO_2_0 = 0b011

# TX
TX_PLL_FSEL_4_0 = 0b00001
TX_PLL_CPSEL_1_0 = 0b01
TX_PLL_LPF_CSSEL_1_0 = 0b01
TX_PLL_LPF_RSEL_1_0 = 0b00
TX_CP_IMR_ENB_7_0 = 0b00000000
PA_SEL_2_0 = 0b000
CLK_DIV_4_0 = 0b10000
TX_SEL_DATAIN_INT = 1
TX_SEL_DATAIN_1_0 = 0b10
TX_SEL_RETCLK_DIV2 = 0
TX_SEL_RETCLK_DIV2_EDGE = 0
TX_PWM_DEL_4_0 = 0b00010
TX_EN_NRZ = 0
TX_EN_PA = 1
TX_EN_CLKOUT = 1
TX_RSTOUT_EDGE_SEL = 0

# RST & TEST
SEL_BBTEST = 0
EN_DIG_RST_FORCE = 0
EN_DIG_RST_OVR = 0
EN_PLL_FORCE = 0
EN_PLL_OVR = 0
EN_PLL_PRECH_FORCE = 0
EN_PLL_PRECH_OVR = 0
EN_PRBS_FORCE = 0
EN_PRBS_OVR = 0
TX_CUTVDD11_FORCE = 0
TX_CUTVDD11_OVR = 0
SEL12M = 0

# ADC
EN_ADCRST = 0
EN_GLOBRST = 0
IAMP1_SEL_3_0 = 0b0001
IAMP2_SEL_3_0 = 0b0001
IAMP3_SEL_3_0 = 0b0001
IAMP4_SEL_3_0 = 0b0100
IBUF1_SEL_3_0 = 0b0001
IBUF2_SEL_3_0 = 0b0001
IBUF3_SEL_3_0 = 0b0001
IBUF4_SEL_3_0 = 0b0001
ICM1_SEL_2_0 = 0b000
ICM2_SEL_2_0 = 0b111
ICM3_SEL_2_0 = 0b111
ICM4_SEL_2_0 = 0b111

# TEST OUT
ENCLK400K = 1
ENCLK33K = 1
ENPKT = 1
ENCH1 = 1
ENCH2 = 1
ENCH3 = 1
ENCH4 = 1
ENCLK200K = 1
ENBBTEST = 0
TX_PA_SEL_3 = 0
EN_CIC = 0
SMP_CLK_DIV_4_0 = 0b00010

no_spare_101_0 = 0b000

# --- Array/List Definitions and Population ---

# Array to contain all (Python list equivalent)
# Initialize sr_fields with a size of 66, filled with zeros
# This allows assignment by index like a C array.
sr_fields = [0] * 66

# Lengths of each field (Python list equivalent)
sr_fields_len = [
    4, 13, 3, 4, 3, 3, 3, 3, 3, 4, 3, 5, 2, 2, 2, 8, 3, 5, 1, 2, 1, 1, 5,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4,
    4, 4, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 95
]

# PMU assignments
sr_fields[0] = PMU_BGR_RSEL_3_0
# sr_fields[1] = offset # Commented out in original C code
sr_fields[1] = PMU_IBN_ENB_12_0
sr_fields[2] = PMU_VDDA_SELB_2_0
sr_fields[3] = PMU_VDDVCO_SELB_3_0
sr_fields[4] = PMU_POR_SEL_2_0
sr_fields[5] = PMU_VDDD_SELB_2_0
sr_fields[6] = PMU_VDDADC_SEL_2_0
sr_fields[7] = PMU_VPA_SEL_2_0
sr_fields[8] = PMU_REFSEL_CM_2_0
sr_fields[9] = PMU_REFSEL_HI_3_0
sr_fields[10] = PMU_REFSEL_LO_2_0

# TX assignments
sr_fields[11] = TX_PLL_FSEL_4_0
sr_fields[12] = TX_PLL_CPSEL_1_0
sr_fields[13] = TX_PLL_LPF_CSSEL_1_0
sr_fields[14] = TX_PLL_LPF_RSEL_1_0
sr_fields[15] = TX_CP_IMR_ENB_7_0
sr_fields[16] = PA_SEL_2_0
sr_fields[17] = CLK_DIV_4_0
sr_fields[18] = TX_SEL_DATAIN_INT
sr_fields[19] = TX_SEL_DATAIN_1_0
sr_fields[20] = TX_SEL_RETCLK_DIV2
sr_fields[21] = TX_SEL_RETCLK_DIV2_EDGE
sr_fields[22] = TX_PWM_DEL_4_0
sr_fields[23] = TX_EN_NRZ
sr_fields[24] = TX_EN_PA
sr_fields[25] = TX_EN_CLKOUT
sr_fields[26] = TX_RSTOUT_EDGE_SEL

# RST & TEST assignments
sr_fields[27] = SEL_BBTEST
sr_fields[28] = EN_DIG_RST_FORCE
sr_fields[29] = EN_DIG_RST_OVR
sr_fields[30] = EN_PLL_FORCE
sr_fields[31] = EN_PLL_OVR
sr_fields[32] = EN_PLL_PRECH_FORCE
sr_fields[33] = EN_PLL_PRECH_OVR
sr_fields[34] = EN_PRBS_FORCE
sr_fields[35] = EN_PRBS_OVR
sr_fields[36] = TX_CUTVDD11_FORCE
sr_fields[37] = TX_CUTVDD11_OVR
sr_fields[38] = SEL12M

# ADC assignments
sr_fields[39] = EN_ADCRST
sr_fields[40] = EN_GLOBRST
sr_fields[41] = IAMP1_SEL_3_0
sr_fields[42] = IAMP2_SEL_3_0
sr_fields[43] = IAMP3_SEL_3_0
sr_fields[44] = IAMP4_SEL_3_0
sr_fields[45] = IBUF1_SEL_3_0
sr_fields[46] = IBUF2_SEL_3_0
sr_fields[47] = IBUF3_SEL_3_0
sr_fields[48] = IBUF4_SEL_3_0
sr_fields[49] = ICM1_SEL_2_0
sr_fields[50] = ICM2_SEL_2_0
sr_fields[51] = ICM3_SEL_2_0
sr_fields[52] = ICM4_SEL_2_0

# TEST OUT assignments
sr_fields[53] = ENCLK400K
sr_fields[54] = ENCLK33K
sr_fields[55] = ENPKT
sr_fields[56] = ENCH1
sr_fields[57] = ENCH2
sr_fields[58] = ENCH3
sr_fields[59] = ENCH4
sr_fields[60] = ENCLK200K
sr_fields[61] = ENBBTEST
sr_fields[62] = TX_PA_SEL_3
sr_fields[63] = EN_CIC
sr_fields[64] = SMP_CLK_DIV_4_0

# sr_fields[62]= offset_2_0; # This line from C code is commented out; assuming it's an old reference or typo for index 62
sr_fields[65] = no_spare_101_0