#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
# SPDX-License-Identifier: Apache-2.0

import os

from extract_utils.fixups_blob import blob_fixup, blob_fixups_user_type
from extract_utils.main import ExtractUtils, ExtractUtilsModule

namespace_imports = [
    'device/motorola/fogos',
    'device/motorola/sm6375-common',
    'hardware/lineage/compat',
    'hardware/motorola',
    'hardware/qcom-caf/sm6375-6.1',
]

blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/sensors.ssc.so': blob_fixup()
        .replace_needed('libsnsapi.so', 'libsnsapi-fogos.so')
        .replace_needed('libssc.so', 'libssc-fogos.so')
        .add_needed('libcompiler_rt.so'),
    'vendor/lib64/libssc-fogos.so': blob_fixup()
        .fix_soname()
        .replace_needed('libsnsapi.so', 'libsnsapi-fogos.so'),
    'vendor/lib64/libmot_chi_desktop_helper.so': blob_fixup()
        .add_needed('libgui_buffer_shim_vendor.so'),
    'vendor/lib64/hw/camera.qcom.so': blob_fixup()
        .replace_needed('libsnsapi.so', 'libsnsapi-fogos.so'),
    'vendor/lib64/libsnsapi-fogos.so': blob_fixup()
        .fix_soname(),
    ('vendor/lib64/camera/components/com.mot.node.c2d.so', 'vendor/lib64/camera/components/com.qti.node.dewarp.so', 'vendor/lib64/camera/components/com.vidhance.node.ica.so', 'vendor/lib64/camera/components/com.vidhance.node.processing.so'): blob_fixup()
        .replace_needed('libui.so', 'libui-v34.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'fogos',
    'motorola',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=False,
    skip_main_proprietary_file=os.environ.get('SM6375_BLOB_SOURCE') == 'malmo',
)

if __name__ == '__main__':
    ExtractUtils.device_with_common(module, 'sm6375-common', module.vendor).run()
