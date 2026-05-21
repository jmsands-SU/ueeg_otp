# eegv5_prog_array.py - GENERATED FROM PROVIDED DATA

sr_fields_len = [
    4, 13, 3, 4, 3, 3, 3, 3, 3, 4, 3, 5, 2, 2, 2, 8, 3, 5, 1, 2, 1, 1, 5,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4,
    4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 5, 83
]

sr_fields = [
    0b1000, # PMU_BGR_RSEL_3_0
    0b0000111111011, # PMU_IBN_ENB_12_0
    0b111, # PMU_VDDA_SELB_2_0
    0b1101, # PMU_VDDVCO_SELB_3_0
    0b000, # PMU_POR_SEL_2_0
    0b100, # PMU_VDDD_SELB_2_0
    0b111, # PMU_VDDADC_SEL_2_0
    0b110, # PMU_VPA_SEL_2_0
    0b011, # PMU_REFSEL_CM_2_0
    0b0010, # PMU_REFSEL_HI_3_0
    0b101, # PMU_REFSEL_LO_2_0
    0b01000, # TX_PLL_FSEL_4_0
    0b01, # TX_PLL_CPSEL_1_0
    0b01, # TX_PLL_LPF_CSSEL_1_0
    0b00, # TX_PLL_LPF_RSEL_1_0
    0b00000000, # TX_CP_IMR_ENB_7_0
    0b110, # PA_SEL_2_0
    0b00100, # CLK_DIV_4_0
    1, # TX_SEL_DATAIN_INT
    0b10, # TX_SEL_DATAIN_1_0
    0, # TX_SEL_RETCLK_DIV2
    0, # TX_SEL_RETCLK_DIV2_EDGE
    0b00001, # TX_PWM_DEL_4_0
    0, # TX_EN_NRZ
    1, # TX_EN_PA
    1, # TX_EN_CLKOUT
    0, # TX_RSTOUT_EDGE_SEL
    0, # SEL_BBTEST
    0, # EN_DIG_RST_FORCE
    0, # EN_DIG_RST_OVR
    0, # EN_PLL_FORCE
    0, # EN_PLL_OVR
    0, # EN_PLL_PRECH_FORCE
    0, # EN_PLL_PRECH_OVR
    0, # EN_PRBS_FORCE
    0, # EN_PRBS_OVR
    0, # TX_CUTVDD11_FORCE
    0, # TX_CUTVDD11_OVR
    0, # SEL12M
    0, # EN_ADCRST
    0, # EN_GLOBRST
    0b1111, # IAMP1_SEL_3_0
    0b1111, # IAMP2_SEL_3_0
    0b1111, # IAMP3_SEL_3_0
    0b1111, # IAMP4_SEL_3_0
    0b1111, # IBUF1_SEL_3_0
    0b1111, # IBUF2_SEL_3_0
    0b1111, # IBUF3_SEL_3_0
    0b1111, # IBUF4_SEL_3_0
    1, # ENCLK400K
    1, # ENCLK33K
    1, # ENPKT
    1, # ENCH1
    1, # ENCH2
    1, # ENCH3
    1, # ENCH4
    1, # ENCLK200K
    0, # ENBBTEST
    1, # CIC_EN
    0b011, # NBIAS_RES_SEL1_2_0
    0b011, # NBIAS_RES_SEL2_2_0
    0b011, # NBIAS_RES_SEL3_2_0
    0b011, # NBIAS_RES_SEL4_2_0
    0b011, # PBIAS_RES_SEL1_2_0
    0b011, # PBIAS_RES_SEL2_2_0
    0b011, # PBIAS_RES_SEL3_2_0
    0b011, # PBIAS_RES_SEL4_2_0
    1, # D12_TX_PA_SEL_3
    0b10000, # D12_SMP_CLK_DIV_4_0
    0b000000000000000000000000000000000000000000000000000, # no_spare_82_0
]
print(sr_fields[8:11])

#PA power is field 16 and 67
#PA enable is field 24
#Duty Cycle is field 22


#amp power is 41:49

