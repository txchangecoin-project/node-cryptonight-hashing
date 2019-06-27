{
    "targets": [
        {
            "target_name": "cryptonight-hashing",
            "sources": [
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/asm/cn_main_loop.S" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/asm/CryptonightR_template.S" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/CryptonightR_gen.cpp" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && (grep avx2 /proc/cpuinfo >/dev/null && echo "xmrig/crypto/cn_gpu_avx.cpp" || echo) || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/cn_gpu_ssse3.cpp" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null || echo "xmrig/crypto/cn_gpu_arm.cpp" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/common/cpu/Cpu.cpp" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/common/cpu/BasicCpuInfo.cpp" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null || echo "xmrig/common/cpu/BasicCpuInfo_arm.cpp" || echo)',
                "multihashing.cc",
                "xmrig/extra.cpp",
                "xmrig/Mem.cpp",
                "xmrig/Mem_unix.cpp",
                "xmrig/crypto/c_blake256.c",
                "xmrig/crypto/c_groestl.c",
                "xmrig/crypto/c_jh.c",
                "xmrig/crypto/c_skein.c",
                "xmrig/common/crypto/keccak.cpp",

                "RandomXL/src/aes_hash.cpp",
                "RandomXL/src/argon2_ref.c",
                "RandomXL/src/dataset.cpp",
                "RandomXL/src/soft_aes.cpp",
                "RandomXL/src/virtual_memory.cpp",
                "RandomXL/src/vm_interpreted.cpp",
                "RandomXL/src/allocator.cpp",
                "RandomXL/src/assembly_generator_x86.cpp",
                "RandomXL/src/instruction.cpp",
                "RandomXL/src/randomx.cpp",
                "RandomXL/src/superscalar.cpp",
                "RandomXL/src/vm_compiled.cpp",
                "RandomXL/src/vm_interpreted_light.cpp",
                "RandomXL/src/argon2_core.c",
                "RandomXL/src/blake2_generator.cpp",
                "RandomXL/src/instructions_portable.cpp",
                "RandomXL/src/reciprocal.c",
                "RandomXL/src/virtual_machine.cpp",
                "RandomXL/src/vm_compiled_light.cpp",
                "RandomXL/src/blake2/blake2b.c",
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "RandomXL/src/jit_compiler_x86_static.S" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "RandomXL/src/jit_compiler_x86.cpp" || echo)',
            ],
            "include_dirs": [
                "xmrig",
                "xmrig/3rdparty",
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_c": [
                '<!@(uname -a | grep "aarch64" >/dev/null && echo "-march=armv8-a+crypto -flax-vector-conversions -DXMRIG_ARM=1" || (uname -a | grep "armv7" >/dev/null && echo "-mfpu=neon -flax-vector-conversions -DXMRIG_ARM=1" || echo "-march=native"))',
                '<!@(grep Intel /proc/cpuinfo >/dev/null && echo -DCPU_INTEL || (grep AMD /proc/cpuinfo >/dev/null && (test `awk \'/cpu family/ && $NF~/^[0-9]*$/ {print $NF}\' /proc/cpuinfo | head -n1` -ge 23 && echo -DAMD || echo -DAMD_OLD) || echo))>',
                "-std=gnu11      -fPIC -DNDEBUG -Ofast -fno-fast-math -w"
            ],
            "cflags_cc": [
                '<!@(uname -a | grep "aarch64" >/dev/null && echo "-march=armv8-a+crypto -flax-vector-conversions -DXMRIG_ARM=1" || (uname -a | grep "armv7" >/dev/null && echo "-mfpu=neon -flax-vector-conversions -DXMRIG_ARM=1" || echo "-march=native"))',
                '<!@(grep Intel /proc/cpuinfo >/dev/null && echo -DCPU_INTEL || (grep AMD /proc/cpuinfo >/dev/null && (test `awk \'/cpu family/ && $NF~/^[0-9]*$/ {print $NF}\' /proc/cpuinfo | head -n1` -ge 23 && echo -DAMD || echo -DAMD_OLD) || echo))>',
                "-std=gnu++11 -s -fPIC -DNDEBUG -Ofast -fno-fast-math -fexceptions -fno-rtti -Wno-class-memaccess -w"
            ]
        }
    ]
}
