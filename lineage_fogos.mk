#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
TARGET_SUPPORTS_OMX_SERVICE := false
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from fogos device
$(call inherit-product, device/motorola/fogos/device.mk)

# Inherit some common Lineage stuff.
TARGET_DISABLE_EPPE := true
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_NAME := lineage_fogos
PRODUCT_DEVICE := fogos
PRODUCT_MANUFACTURER := motorola
PRODUCT_BRAND := motorola
PRODUCT_MODEL := moto g34 5G

# AxionOS stuff
TARGET_INCLUDE_AXFX := false
TARGET_ENABLE_BLUR := true
AXION_CAMERA_REAR_INFO := 50,2
AXION_CAMERA_FRONT_INFO := 16
AXION_MAINTAINER := Hen
AXION_PROCESSOR := Snapdragon_695

# kernel
WITH_KSU := true

PRODUCT_GMS_CLIENTID_BASE := android-motorola

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="fogos_g-user 15 V1UGS35H.75-14-3-8 4be56-0d815a release-keys MV-186" \
    BuildFingerprint=motorola/fogos_g/fogos:15/V1UGS35H.75-14-3-8/4be56-0d815a:user/release-keys \
    DeviceProduct=fogos_g
