# Copyright (c) 2011 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'target_defaults': {
    'configurations': {
      'Debug': {
        'defines': [
          'DEBUG',
          '_DEBUG',
        ],
      },
      'Release': {
        'defines': [
          'NDEBUG',
        ],
      },
    },
    'conditions': [
      ['OS=="win"', {
        'configurations': {
          'Common_Base': {
            'msvs_configuration_attributes': {
              # Do not compile NSPR and NSS with /D _UNICODE /D UNICODE.
              'CharacterSet': '0'
            }
          }
        },
        'defines!': [
          'WIN32_LEAN_AND_MEAN',
        ],
      }],
    ],
  },
  'targets': [
    {
      'target_name': 'nspr',
      'type': '<(library)',
      'sources': [
        'mozilla/nsprpub/lib/ds/plarena.c',
        'mozilla/nsprpub/lib/ds/plarena.h',
        'mozilla/nsprpub/lib/ds/plarenas.h',
        'mozilla/nsprpub/lib/ds/plhash.c',
        'mozilla/nsprpub/lib/ds/plhash.h',
        'mozilla/nsprpub/lib/libc/include/plbase64.h',
        'mozilla/nsprpub/lib/libc/include/plerror.h',
        'mozilla/nsprpub/lib/libc/include/plgetopt.h',
        'mozilla/nsprpub/lib/libc/include/plstr.h',
        'mozilla/nsprpub/lib/libc/src/base64.c',
        'mozilla/nsprpub/lib/libc/src/plerror.c',
        'mozilla/nsprpub/lib/libc/src/plgetopt.c',
        'mozilla/nsprpub/lib/libc/src/strcase.c',
        'mozilla/nsprpub/lib/libc/src/strcat.c',
        'mozilla/nsprpub/lib/libc/src/strchr.c',
        'mozilla/nsprpub/lib/libc/src/strcmp.c',
        'mozilla/nsprpub/lib/libc/src/strcpy.c',
        'mozilla/nsprpub/lib/libc/src/strdup.c',
        'mozilla/nsprpub/lib/libc/src/strlen.c',
        'mozilla/nsprpub/lib/libc/src/strpbrk.c',
        'mozilla/nsprpub/lib/libc/src/strstr.c',
        'mozilla/nsprpub/lib/libc/src/strtok.c',
        'mozilla/nsprpub/pr/include/md/prosdep.h',
        'mozilla/nsprpub/pr/include/md/_darwin.cfg',
        'mozilla/nsprpub/pr/include/md/_darwin.h',
        'mozilla/nsprpub/pr/include/md/_pcos.h',
        'mozilla/nsprpub/pr/include/md/_pth.h',
        'mozilla/nsprpub/pr/include/md/_unixos.h',
        'mozilla/nsprpub/pr/include/md/_unix_errors.h',
        'mozilla/nsprpub/pr/include/md/_win32_errors.h',
        'mozilla/nsprpub/pr/include/md/_win95.cfg',
        'mozilla/nsprpub/pr/include/md/_win95.h',
        'mozilla/nsprpub/pr/include/nspr.h',
        'mozilla/nsprpub/pr/include/obsolete/pralarm.h',
        'mozilla/nsprpub/pr/include/obsolete/probslet.h',
        'mozilla/nsprpub/pr/include/obsolete/protypes.h',
        'mozilla/nsprpub/pr/include/obsolete/prsem.h',
        'mozilla/nsprpub/pr/include/pratom.h',
        'mozilla/nsprpub/pr/include/prbit.h',
        'mozilla/nsprpub/pr/include/prclist.h',
        'mozilla/nsprpub/pr/include/prcmon.h',
        'mozilla/nsprpub/pr/include/prcountr.h',
        'mozilla/nsprpub/pr/include/prcpucfg.h',
        'mozilla/nsprpub/pr/include/prcvar.h',
        'mozilla/nsprpub/pr/include/prdtoa.h',
        'mozilla/nsprpub/pr/include/prenv.h',
        'mozilla/nsprpub/pr/include/prerr.h',
        'mozilla/nsprpub/pr/include/prerror.h',
        'mozilla/nsprpub/pr/include/prinet.h',
        'mozilla/nsprpub/pr/include/prinit.h',
        'mozilla/nsprpub/pr/include/prinrval.h',
        'mozilla/nsprpub/pr/include/prio.h',
        'mozilla/nsprpub/pr/include/pripcsem.h',
        'mozilla/nsprpub/pr/include/private/pprio.h',
        'mozilla/nsprpub/pr/include/private/pprmwait.h',
        'mozilla/nsprpub/pr/include/private/pprthred.h',
        'mozilla/nsprpub/pr/include/private/primpl.h',
        'mozilla/nsprpub/pr/include/private/prpriv.h',
        'mozilla/nsprpub/pr/include/prlink.h',
        'mozilla/nsprpub/pr/include/prlock.h',
        'mozilla/nsprpub/pr/include/prlog.h',
        'mozilla/nsprpub/pr/include/prlong.h',
        'mozilla/nsprpub/pr/include/prmem.h',
        'mozilla/nsprpub/pr/include/prmon.h',
        'mozilla/nsprpub/pr/include/prmwait.h',
        'mozilla/nsprpub/pr/include/prnetdb.h',
        'mozilla/nsprpub/pr/include/prolock.h',
        'mozilla/nsprpub/pr/include/prpdce.h',
        'mozilla/nsprpub/pr/include/prprf.h',
        'mozilla/nsprpub/pr/include/prproces.h',
        'mozilla/nsprpub/pr/include/prrng.h',
        'mozilla/nsprpub/pr/include/prrwlock.h',
        'mozilla/nsprpub/pr/include/prshm.h',
        'mozilla/nsprpub/pr/include/prshma.h',
        'mozilla/nsprpub/pr/include/prsystem.h',
        'mozilla/nsprpub/pr/include/prthread.h',
        'mozilla/nsprpub/pr/include/prtime.h',
        'mozilla/nsprpub/pr/include/prtpool.h',
        'mozilla/nsprpub/pr/include/prtrace.h',
        'mozilla/nsprpub/pr/include/prtypes.h',
        'mozilla/nsprpub/pr/include/prvrsion.h',
        'mozilla/nsprpub/pr/include/prwin16.h',
        'mozilla/nsprpub/pr/src/io/prdir.c',
        'mozilla/nsprpub/pr/src/io/prfdcach.c',
        'mozilla/nsprpub/pr/src/io/prfile.c',
        'mozilla/nsprpub/pr/src/io/prio.c',
        'mozilla/nsprpub/pr/src/io/priometh.c',
        'mozilla/nsprpub/pr/src/io/pripv6.c',
        'mozilla/nsprpub/pr/src/io/prlayer.c',
        'mozilla/nsprpub/pr/src/io/prlog.c',
        'mozilla/nsprpub/pr/src/io/prmapopt.c',
        'mozilla/nsprpub/pr/src/io/prmmap.c',
        'mozilla/nsprpub/pr/src/io/prmwait.c',
        'mozilla/nsprpub/pr/src/io/prpolevt.c',
        'mozilla/nsprpub/pr/src/io/prprf.c',
        'mozilla/nsprpub/pr/src/io/prscanf.c',
        'mozilla/nsprpub/pr/src/io/prsocket.c',
        'mozilla/nsprpub/pr/src/io/prstdio.c',
        'mozilla/nsprpub/pr/src/linking/prlink.c',
        'mozilla/nsprpub/pr/src/malloc/prmalloc.c',
        'mozilla/nsprpub/pr/src/malloc/prmem.c',
        'mozilla/nsprpub/pr/src/md/prosdep.c',
        'mozilla/nsprpub/pr/src/md/unix/darwin.c',
        'mozilla/nsprpub/pr/src/md/unix/os_Darwin.s',
        'mozilla/nsprpub/pr/src/md/unix/os_Darwin_x86.s',
        'mozilla/nsprpub/pr/src/md/unix/os_Darwin_x86_64.s',
        'mozilla/nsprpub/pr/src/md/unix/unix.c',
        'mozilla/nsprpub/pr/src/md/unix/unix_errors.c',
        'mozilla/nsprpub/pr/src/md/unix/uxproces.c',
        'mozilla/nsprpub/pr/src/md/unix/uxrng.c',
        'mozilla/nsprpub/pr/src/md/unix/uxshm.c',
        'mozilla/nsprpub/pr/src/md/unix/uxwrap.c',
        'mozilla/nsprpub/pr/src/md/windows/ntgc.c',
        'mozilla/nsprpub/pr/src/md/windows/ntinrval.c',
        'mozilla/nsprpub/pr/src/md/windows/ntmisc.c',
        'mozilla/nsprpub/pr/src/md/windows/ntsec.c',
        'mozilla/nsprpub/pr/src/md/windows/ntsem.c',
        'mozilla/nsprpub/pr/src/md/windows/w32ipcsem.c',
        'mozilla/nsprpub/pr/src/md/windows/w32poll.c',
        'mozilla/nsprpub/pr/src/md/windows/w32rng.c',
        'mozilla/nsprpub/pr/src/md/windows/w32shm.c',
        'mozilla/nsprpub/pr/src/md/windows/w95cv.c',
        'mozilla/nsprpub/pr/src/md/windows/w95dllmain.c',
        'mozilla/nsprpub/pr/src/md/windows/w95io.c',
        'mozilla/nsprpub/pr/src/md/windows/w95sock.c',
        'mozilla/nsprpub/pr/src/md/windows/w95thred.c',
        'mozilla/nsprpub/pr/src/md/windows/win32_errors.c',
        'mozilla/nsprpub/pr/src/memory/prseg.c',
        'mozilla/nsprpub/pr/src/memory/prshm.c',
        'mozilla/nsprpub/pr/src/memory/prshma.c',
        'mozilla/nsprpub/pr/src/misc/pralarm.c',
        'mozilla/nsprpub/pr/src/misc/pratom.c',
        'mozilla/nsprpub/pr/src/misc/praton.c',
        'mozilla/nsprpub/pr/src/misc/prcountr.c',
        'mozilla/nsprpub/pr/src/misc/prdtoa.c',
        'mozilla/nsprpub/pr/src/misc/prenv.c',
        'mozilla/nsprpub/pr/src/misc/prerr.c',
        'mozilla/nsprpub/pr/src/misc/prerror.c',
        'mozilla/nsprpub/pr/src/misc/prerrortable.c',
        'mozilla/nsprpub/pr/src/misc/prinit.c',
        'mozilla/nsprpub/pr/src/misc/prinrval.c',
        'mozilla/nsprpub/pr/src/misc/pripc.c',
        'mozilla/nsprpub/pr/src/misc/pripcsem.c',
        'mozilla/nsprpub/pr/src/misc/prlog2.c',
        'mozilla/nsprpub/pr/src/misc/prlong.c',
        'mozilla/nsprpub/pr/src/misc/prnetdb.c',
        'mozilla/nsprpub/pr/src/misc/prolock.c',
        'mozilla/nsprpub/pr/src/misc/prrng.c',
        'mozilla/nsprpub/pr/src/misc/prsystem.c',
        'mozilla/nsprpub/pr/src/misc/prthinfo.c',
        'mozilla/nsprpub/pr/src/misc/prtime.c',
        'mozilla/nsprpub/pr/src/misc/prtpool.c',
        'mozilla/nsprpub/pr/src/misc/prtrace.c',
        'mozilla/nsprpub/pr/src/pthreads/ptio.c',
        'mozilla/nsprpub/pr/src/pthreads/ptmisc.c',
        'mozilla/nsprpub/pr/src/pthreads/ptsynch.c',
        'mozilla/nsprpub/pr/src/pthreads/ptthread.c',
        'mozilla/nsprpub/pr/src/threads/combined/prucpu.c',
        'mozilla/nsprpub/pr/src/threads/combined/prucv.c',
        'mozilla/nsprpub/pr/src/threads/combined/prulock.c',
        'mozilla/nsprpub/pr/src/threads/combined/prustack.c',
        'mozilla/nsprpub/pr/src/threads/combined/pruthr.c',
        'mozilla/nsprpub/pr/src/threads/prcmon.c',
        'mozilla/nsprpub/pr/src/threads/prcthr.c',
        'mozilla/nsprpub/pr/src/threads/prdump.c',
        'mozilla/nsprpub/pr/src/threads/prmon.c',
        'mozilla/nsprpub/pr/src/threads/prrwlock.c',
        'mozilla/nsprpub/pr/src/threads/prsem.c',
        'mozilla/nsprpub/pr/src/threads/prtpd.c',
      ],
      'defines': [
        'FORCE_PR_LOG',
      ],
      'include_dirs': [
        'mozilla/nsprpub/pr/include',
        'mozilla/nsprpub/pr/include/private',
        'mozilla/nsprpub/lib/ds',
        'mozilla/nsprpub/lib/libc/include',
      ],
      'direct_dependent_settings': {
        'defines': [
          'NO_NSPR_10_SUPPORT',
        ],
        'include_dirs': [
          'mozilla/nsprpub/pr/include',
          'mozilla/nsprpub/lib/ds',
          'mozilla/nsprpub/lib/libc/include',
        ],
      },
      # TODO(wtc): suppress C4244 and C4554 in prdtoa.c.
      'msvs_disabled_warnings': [4018, 4244, 4554],
      'conditions': [
        ['OS=="mac"', {
          'defines': [
            'XP_UNIX',
            'DARWIN',
            'XP_MACOSX',
            '_PR_PTHREADS',
            'HAVE_BSD_FLOCK',
            'HAVE_SOCKLEN_T',
            'HAVE_LCHOWN',
            'HAVE_STRERROR',
          ],
          'sources/': [
            ['exclude', '^mozilla/nsprpub/pr/src/md/windows/'],
            ['exclude', '^mozilla/nsprpub/pr/src/threads/combined/'],
          ],
          'sources!': [
            'mozilla/nsprpub/pr/src/io/prdir.c',
            'mozilla/nsprpub/pr/src/io/prfile.c',
            'mozilla/nsprpub/pr/src/io/prio.c',
            'mozilla/nsprpub/pr/src/io/prsocket.c',
            # os_Darwin_x86.s and os_Darwin_x86_64.s are included by
            # os_Darwin.s.
            'mozilla/nsprpub/pr/src/md/unix/os_Darwin_x86.s',
            'mozilla/nsprpub/pr/src/md/unix/os_Darwin_x86_64.s',
            'mozilla/nsprpub/pr/src/misc/pripcsem.c',
            'mozilla/nsprpub/pr/src/threads/prcthr.c',
            'mozilla/nsprpub/pr/src/threads/prdump.c',
            'mozilla/nsprpub/pr/src/threads/prmon.c',
            'mozilla/nsprpub/pr/src/threads/prsem.c',
          ],
        }],
        ['OS=="win"', {
          'defines': [
            'XP_PC',
            'WIN32',
            'WIN95',
            '_PR_GLOBAL_THREADS_ONLY',
          ],
          'sources/': [
            ['exclude', '^mozilla/nsprpub/pr/src/md/unix/'],
            ['exclude', '^mozilla/nsprpub/pr/src/pthreads/'],
          ],
          'conditions': [
            ['target_arch=="ia32"', {
              'defines': [
                '_X86_',
              ],
            }],
          ],
        }],
      ],
    },
    {
      'target_name': 'nss',
      'type': '<(library)',
      'sources': [
        'mozilla/security/nss/lib/base/arena.c',
        'mozilla/security/nss/lib/base/base.h',
        'mozilla/security/nss/lib/base/baset.h',
        'mozilla/security/nss/lib/base/error.c',
        'mozilla/security/nss/lib/base/errorval.c',
        'mozilla/security/nss/lib/base/hash.c',
        'mozilla/security/nss/lib/base/hashops.c',
        'mozilla/security/nss/lib/base/item.c',
        'mozilla/security/nss/lib/base/libc.c',
        'mozilla/security/nss/lib/base/list.c',
        'mozilla/security/nss/lib/base/nssbase.h',
        'mozilla/security/nss/lib/base/nssbaset.h',
        'mozilla/security/nss/lib/base/nssutf8.c',
        'mozilla/security/nss/lib/base/tracker.c',
        'mozilla/security/nss/lib/certdb/alg1485.c',
        'mozilla/security/nss/lib/certdb/cert.h',
        'mozilla/security/nss/lib/certdb/certdb.c',
        'mozilla/security/nss/lib/certdb/certdb.h',
        'mozilla/security/nss/lib/certdb/certi.h',
        'mozilla/security/nss/lib/certdb/certt.h',
        'mozilla/security/nss/lib/certdb/certv3.c',
        'mozilla/security/nss/lib/certdb/certxutl.c',
        'mozilla/security/nss/lib/certdb/certxutl.h',
        'mozilla/security/nss/lib/certdb/crl.c',
        'mozilla/security/nss/lib/certdb/genname.c',
        'mozilla/security/nss/lib/certdb/genname.h',
        'mozilla/security/nss/lib/certdb/polcyxtn.c',
        'mozilla/security/nss/lib/certdb/secname.c',
        'mozilla/security/nss/lib/certdb/stanpcertdb.c',
        'mozilla/security/nss/lib/certdb/xauthkid.c',
        'mozilla/security/nss/lib/certdb/xbsconst.c',
        'mozilla/security/nss/lib/certdb/xconst.c',
        'mozilla/security/nss/lib/certdb/xconst.h',
        'mozilla/security/nss/lib/certhigh/certhigh.c',
        'mozilla/security/nss/lib/certhigh/certhtml.c',
        'mozilla/security/nss/lib/certhigh/certreq.c',
        'mozilla/security/nss/lib/certhigh/certvfy.c',
        'mozilla/security/nss/lib/certhigh/crlv2.c',
        'mozilla/security/nss/lib/certhigh/ocsp.c',
        'mozilla/security/nss/lib/certhigh/ocsp.h',
        'mozilla/security/nss/lib/certhigh/ocspi.h',
        'mozilla/security/nss/lib/certhigh/ocspt.h',
        'mozilla/security/nss/lib/certhigh/ocspti.h',
        'mozilla/security/nss/lib/certhigh/xcrldist.c',
        'mozilla/security/nss/lib/cryptohi/cryptohi.h',
        'mozilla/security/nss/lib/cryptohi/cryptoht.h',
        'mozilla/security/nss/lib/cryptohi/dsautil.c',
        'mozilla/security/nss/lib/cryptohi/key.h',
        'mozilla/security/nss/lib/cryptohi/keyhi.h',
        'mozilla/security/nss/lib/cryptohi/keyi.h',
        'mozilla/security/nss/lib/cryptohi/keyt.h',
        'mozilla/security/nss/lib/cryptohi/keythi.h',
        'mozilla/security/nss/lib/cryptohi/sechash.c',
        'mozilla/security/nss/lib/cryptohi/seckey.c',
        'mozilla/security/nss/lib/cryptohi/secsign.c',
        'mozilla/security/nss/lib/cryptohi/secvfy.c',
        'mozilla/security/nss/lib/dev/ckhelper.c',
        'mozilla/security/nss/lib/dev/ckhelper.h',
        'mozilla/security/nss/lib/dev/dev.h',
        'mozilla/security/nss/lib/dev/devm.h',
        'mozilla/security/nss/lib/dev/devslot.c',
        'mozilla/security/nss/lib/dev/devt.h',
        'mozilla/security/nss/lib/dev/devtm.h',
        'mozilla/security/nss/lib/dev/devtoken.c',
        'mozilla/security/nss/lib/dev/devutil.c',
        'mozilla/security/nss/lib/dev/nssdev.h',
        'mozilla/security/nss/lib/dev/nssdevt.h',
        'mozilla/security/nss/lib/freebl/aeskeywrap.c',
        'mozilla/security/nss/lib/freebl/alg2268.c',
        'mozilla/security/nss/lib/freebl/alghmac.c',
        'mozilla/security/nss/lib/freebl/alghmac.h',
        'mozilla/security/nss/lib/freebl/arcfive.c',
        'mozilla/security/nss/lib/freebl/arcfour.c',
        'mozilla/security/nss/lib/freebl/blapi.h',
        'mozilla/security/nss/lib/freebl/blapii.h',
        'mozilla/security/nss/lib/freebl/blapit.h',
        'mozilla/security/nss/lib/freebl/camellia.c',
        'mozilla/security/nss/lib/freebl/camellia.h',
        'mozilla/security/nss/lib/freebl/des.c',
        'mozilla/security/nss/lib/freebl/des.h',
        'mozilla/security/nss/lib/freebl/desblapi.c',
        'mozilla/security/nss/lib/freebl/dh.c',
        'mozilla/security/nss/lib/freebl/drbg.c',
        'mozilla/security/nss/lib/freebl/dsa.c',
        'mozilla/security/nss/lib/freebl/ec.c',
        'mozilla/security/nss/lib/freebl/ec.h',
        'mozilla/security/nss/lib/freebl/ecl/ec2.h',
        'mozilla/security/nss/lib/freebl/ecl/ecl-curve.h',
        'mozilla/security/nss/lib/freebl/ecl/ecl-exp.h',
        'mozilla/security/nss/lib/freebl/ecl/ecl-priv.h',
        'mozilla/security/nss/lib/freebl/ecl/ecl.c',
        'mozilla/security/nss/lib/freebl/ecl/ecl.h',
        'mozilla/security/nss/lib/freebl/ecl/ecl_curve.c',
        'mozilla/security/nss/lib/freebl/ecl/ecl_gf.c',
        'mozilla/security/nss/lib/freebl/ecl/ecl_mult.c',
        'mozilla/security/nss/lib/freebl/ecl/ecp.h',
        'mozilla/security/nss/lib/freebl/ecl/ecp_aff.c',
        'mozilla/security/nss/lib/freebl/ecl/ecp_jac.c',
        'mozilla/security/nss/lib/freebl/ecl/ecp_jm.c',
        'mozilla/security/nss/lib/freebl/ecl/ecp_mont.c',
        'mozilla/security/nss/lib/freebl/ecl/ec_naf.c',
        'mozilla/security/nss/lib/freebl/hasht.h',
        'mozilla/security/nss/lib/freebl/md2.c',
        'mozilla/security/nss/lib/freebl/md5.c',
        'mozilla/security/nss/lib/freebl/mpi/logtab.h',
        'mozilla/security/nss/lib/freebl/mpi/mpcpucache.c',
        'mozilla/security/nss/lib/freebl/mpi/mpi-config.h',
        'mozilla/security/nss/lib/freebl/mpi/mpi-priv.h',
        'mozilla/security/nss/lib/freebl/mpi/mpi.c',
        'mozilla/security/nss/lib/freebl/mpi/mpi.h',
        'mozilla/security/nss/lib/freebl/mpi/mpi_amd64.c',
        'mozilla/security/nss/lib/freebl/mpi/mpi_x86_asm.c',
        'mozilla/security/nss/lib/freebl/mpi/mplogic.c',
        'mozilla/security/nss/lib/freebl/mpi/mplogic.h',
        'mozilla/security/nss/lib/freebl/mpi/mpmontg.c',
        'mozilla/security/nss/lib/freebl/mpi/mpprime.c',
        'mozilla/security/nss/lib/freebl/mpi/mpprime.h',
        'mozilla/security/nss/lib/freebl/mpi/mp_gf2m-priv.h',
        'mozilla/security/nss/lib/freebl/mpi/mp_gf2m.c',
        'mozilla/security/nss/lib/freebl/mpi/mp_gf2m.h',
        'mozilla/security/nss/lib/freebl/mpi/primes.c',
        'mozilla/security/nss/lib/freebl/pqg.c',
        'mozilla/security/nss/lib/freebl/rawhash.c',
        'mozilla/security/nss/lib/freebl/rijndael.c',
        'mozilla/security/nss/lib/freebl/rijndael.h',
        'mozilla/security/nss/lib/freebl/rijndael32.tab',
        'mozilla/security/nss/lib/freebl/rsa.c',
        'mozilla/security/nss/lib/freebl/sechash.h',
        'mozilla/security/nss/lib/freebl/secmpi.h',
        'mozilla/security/nss/lib/freebl/secrng.h',
        'mozilla/security/nss/lib/freebl/seed.c',
        'mozilla/security/nss/lib/freebl/seed.h',
        'mozilla/security/nss/lib/freebl/sha256.h',
        'mozilla/security/nss/lib/freebl/sha512.c',
        'mozilla/security/nss/lib/freebl/sha_fast.c',
        'mozilla/security/nss/lib/freebl/sha_fast.h',
        'mozilla/security/nss/lib/freebl/shsign.h',
        'mozilla/security/nss/lib/freebl/shvfy.c',
        'mozilla/security/nss/lib/freebl/sysrand.c',
        'mozilla/security/nss/lib/freebl/tlsprfalg.c',
        'mozilla/security/nss/lib/freebl/unix_rand.c',
        'mozilla/security/nss/lib/freebl/win_rand.c',
        'mozilla/security/nss/lib/nss/nss.h',
        'mozilla/security/nss/lib/nss/nssinit.c',
        'mozilla/security/nss/lib/nss/nssrenam.h',
        'mozilla/security/nss/lib/nss/nssver.c',
        'mozilla/security/nss/lib/nss/utilwrap.c',
        'mozilla/security/nss/lib/pk11wrap/debug_module.c',
        'mozilla/security/nss/lib/pk11wrap/dev3hack.c',
        'mozilla/security/nss/lib/pk11wrap/dev3hack.h',
        'mozilla/security/nss/lib/pk11wrap/pk11akey.c',
        'mozilla/security/nss/lib/pk11wrap/pk11auth.c',
        'mozilla/security/nss/lib/pk11wrap/pk11cert.c',
        'mozilla/security/nss/lib/pk11wrap/pk11cxt.c',
        'mozilla/security/nss/lib/pk11wrap/pk11err.c',
        'mozilla/security/nss/lib/pk11wrap/pk11func.h',
        'mozilla/security/nss/lib/pk11wrap/pk11kea.c',
        'mozilla/security/nss/lib/pk11wrap/pk11list.c',
        'mozilla/security/nss/lib/pk11wrap/pk11load.c',
        'mozilla/security/nss/lib/pk11wrap/pk11mech.c',
        'mozilla/security/nss/lib/pk11wrap/pk11merge.c',
        'mozilla/security/nss/lib/pk11wrap/pk11nobj.c',
        'mozilla/security/nss/lib/pk11wrap/pk11obj.c',
        'mozilla/security/nss/lib/pk11wrap/pk11pars.c',
        'mozilla/security/nss/lib/pk11wrap/pk11pbe.c',
        'mozilla/security/nss/lib/pk11wrap/pk11pk12.c',
        'mozilla/security/nss/lib/pk11wrap/pk11pqg.c',
        'mozilla/security/nss/lib/pk11wrap/pk11pqg.h',
        'mozilla/security/nss/lib/pk11wrap/pk11priv.h',
        'mozilla/security/nss/lib/pk11wrap/pk11pub.h',
        'mozilla/security/nss/lib/pk11wrap/pk11sdr.c',
        'mozilla/security/nss/lib/pk11wrap/pk11sdr.h',
        'mozilla/security/nss/lib/pk11wrap/pk11skey.c',
        'mozilla/security/nss/lib/pk11wrap/pk11slot.c',
        'mozilla/security/nss/lib/pk11wrap/pk11util.c',
        'mozilla/security/nss/lib/pk11wrap/secmod.h',
        'mozilla/security/nss/lib/pk11wrap/secmodi.h',
        'mozilla/security/nss/lib/pk11wrap/secmodti.h',
        'mozilla/security/nss/lib/pk11wrap/secpkcs5.h',
        'mozilla/security/nss/lib/pkcs7/certread.c',
        'mozilla/security/nss/lib/pkcs7/p7common.c',
        'mozilla/security/nss/lib/pkcs7/p7create.c',
        'mozilla/security/nss/lib/pkcs7/p7decode.c',
        'mozilla/security/nss/lib/pkcs7/p7encode.c',
        'mozilla/security/nss/lib/pkcs7/p7local.c',
        'mozilla/security/nss/lib/pkcs7/p7local.h',
        'mozilla/security/nss/lib/pkcs7/pkcs7t.h',
        'mozilla/security/nss/lib/pkcs7/secmime.c',
        'mozilla/security/nss/lib/pkcs7/secmime.h',
        'mozilla/security/nss/lib/pkcs7/secpkcs7.h',
        'mozilla/security/nss/lib/pki/asymmkey.c',
        'mozilla/security/nss/lib/pki/certdecode.c',
        'mozilla/security/nss/lib/pki/certificate.c',
        'mozilla/security/nss/lib/pki/cryptocontext.c',
        'mozilla/security/nss/lib/pki/nsspki.h',
        'mozilla/security/nss/lib/pki/nsspkit.h',
        'mozilla/security/nss/lib/pki/pki.h',
        'mozilla/security/nss/lib/pki/pki3hack.c',
        'mozilla/security/nss/lib/pki/pki3hack.h',
        'mozilla/security/nss/lib/pki/pkibase.c',
        'mozilla/security/nss/lib/pki/pkim.h',
        'mozilla/security/nss/lib/pki/pkistore.c',
        'mozilla/security/nss/lib/pki/pkistore.h',
        'mozilla/security/nss/lib/pki/pkit.h',
        'mozilla/security/nss/lib/pki/pkitm.h',
        'mozilla/security/nss/lib/pki/symmkey.c',
        'mozilla/security/nss/lib/pki/tdcache.c',
        'mozilla/security/nss/lib/pki/trustdomain.c',
        'mozilla/security/nss/lib/smime/cms.h',
        'mozilla/security/nss/lib/smime/cmslocal.h',
        'mozilla/security/nss/lib/smime/cmsreclist.h',
        'mozilla/security/nss/lib/smime/cmst.h',
        'mozilla/security/nss/lib/smime/smime.h',
        'mozilla/security/nss/lib/softoken/ecdecode.c',
        'mozilla/security/nss/lib/softoken/fipsaudt.c',
        'mozilla/security/nss/lib/softoken/fipstest.c',
        'mozilla/security/nss/lib/softoken/fipstokn.c',
        'mozilla/security/nss/lib/softoken/lgglue.c',
        'mozilla/security/nss/lib/softoken/lgglue.h',
        'mozilla/security/nss/lib/softoken/lowkey.c',
        'mozilla/security/nss/lib/softoken/lowkeyi.h',
        'mozilla/security/nss/lib/softoken/lowkeyti.h',
        'mozilla/security/nss/lib/softoken/lowpbe.c',
        'mozilla/security/nss/lib/softoken/lowpbe.h',
        'mozilla/security/nss/lib/softoken/padbuf.c',
        'mozilla/security/nss/lib/softoken/pk11init.h',
        'mozilla/security/nss/lib/softoken/pk11pars.h',
        'mozilla/security/nss/lib/softoken/pkcs11.c',
        'mozilla/security/nss/lib/softoken/pkcs11c.c',
        'mozilla/security/nss/lib/softoken/pkcs11i.h',
        'mozilla/security/nss/lib/softoken/pkcs11ni.h',
        'mozilla/security/nss/lib/softoken/pkcs11u.c',
        'mozilla/security/nss/lib/softoken/rsawrapr.c',
        'mozilla/security/nss/lib/softoken/sdb.c',
        'mozilla/security/nss/lib/softoken/sdb.h',
        'mozilla/security/nss/lib/softoken/secmodt.h',
        'mozilla/security/nss/lib/softoken/sftkdb.c',
        'mozilla/security/nss/lib/softoken/sftkdb.h',
        'mozilla/security/nss/lib/softoken/sftkdbt.h',
        'mozilla/security/nss/lib/softoken/sftkdbti.h',
        'mozilla/security/nss/lib/softoken/sftkmod.c',
        'mozilla/security/nss/lib/softoken/sftkpars.c',
        'mozilla/security/nss/lib/softoken/sftkpars.h',
        'mozilla/security/nss/lib/softoken/sftkpwd.c',
        'mozilla/security/nss/lib/softoken/softkver.c',
        'mozilla/security/nss/lib/softoken/softkver.h',
        'mozilla/security/nss/lib/softoken/softoken.h',
        'mozilla/security/nss/lib/softoken/softoknt.h',
        'mozilla/security/nss/lib/softoken/tlsprf.c',
        'mozilla/security/nss/lib/ssl/sslerr.h',
        'mozilla/security/nss/lib/util/base64.h',
        'mozilla/security/nss/lib/util/ciferfam.h',
        'mozilla/security/nss/lib/util/derdec.c',
        'mozilla/security/nss/lib/util/derenc.c',
        'mozilla/security/nss/lib/util/dersubr.c',
        'mozilla/security/nss/lib/util/dertime.c',
        'mozilla/security/nss/lib/util/nssb64.h',
        'mozilla/security/nss/lib/util/nssb64d.c',
        'mozilla/security/nss/lib/util/nssb64e.c',
        'mozilla/security/nss/lib/util/nssb64t.h',
        'mozilla/security/nss/lib/util/nssilckt.h',
        'mozilla/security/nss/lib/util/nssilock.c',
        'mozilla/security/nss/lib/util/nssilock.h',
        'mozilla/security/nss/lib/util/nsslocks.h',
        'mozilla/security/nss/lib/util/nssrwlk.c',
        'mozilla/security/nss/lib/util/nssrwlk.h',
        'mozilla/security/nss/lib/util/nssrwlkt.h',
        'mozilla/security/nss/lib/util/nssutil.h',
        'mozilla/security/nss/lib/util/oidstring.c',
        'mozilla/security/nss/lib/util/pkcs11.h',
        'mozilla/security/nss/lib/util/pkcs11f.h',
        'mozilla/security/nss/lib/util/pkcs11n.h',
        'mozilla/security/nss/lib/util/pkcs11p.h',
        'mozilla/security/nss/lib/util/pkcs11t.h',
        'mozilla/security/nss/lib/util/pkcs11u.h',
        'mozilla/security/nss/lib/util/portreg.c',
        'mozilla/security/nss/lib/util/portreg.h',
        'mozilla/security/nss/lib/util/quickder.c',
        'mozilla/security/nss/lib/util/secalgid.c',
        'mozilla/security/nss/lib/util/secasn1.h',
        'mozilla/security/nss/lib/util/secasn1d.c',
        'mozilla/security/nss/lib/util/secasn1e.c',
        'mozilla/security/nss/lib/util/secasn1t.h',
        'mozilla/security/nss/lib/util/secasn1u.c',
        'mozilla/security/nss/lib/util/seccomon.h',
        'mozilla/security/nss/lib/util/secder.h',
        'mozilla/security/nss/lib/util/secdert.h',
        'mozilla/security/nss/lib/util/secdig.c',
        'mozilla/security/nss/lib/util/secdig.h',
        'mozilla/security/nss/lib/util/secdigt.h',
        'mozilla/security/nss/lib/util/secerr.h',
        'mozilla/security/nss/lib/util/secitem.c',
        'mozilla/security/nss/lib/util/secitem.h',
        'mozilla/security/nss/lib/util/secoid.c',
        'mozilla/security/nss/lib/util/secoid.h',
        'mozilla/security/nss/lib/util/secoidt.h',
        'mozilla/security/nss/lib/util/secport.c',
        'mozilla/security/nss/lib/util/secport.h',
        'mozilla/security/nss/lib/util/sectime.c',
        'mozilla/security/nss/lib/util/templates.c',
        'mozilla/security/nss/lib/util/utf8.c',
        'mozilla/security/nss/lib/util/utilrename.h',
      ],
      'sources!': [
        # primes.c is included by mpprime.c.
        'mozilla/security/nss/lib/freebl/mpi/primes.c',
        # unix_rand.c and win_rand.c are included by sysrand.c.
        'mozilla/security/nss/lib/freebl/unix_rand.c',
        'mozilla/security/nss/lib/freebl/win_rand.c',
        # debug_module.c is included by pk11load.c.
        'mozilla/security/nss/lib/pk11wrap/debug_module.c',
      ],
      'defines': [
        'NSS_ENABLE_ECC',
        'USE_UTIL_DIRECTLY',
        'MP_API_COMPATIBLE',
        'RIJNDAEL_INCLUDE_TABLES',
        'NSS_USE_STATIC_LIBS',
        'SHLIB_VERSION=\"3\"',
        'SOFTOKEN_SHLIB_VERSION=\"3\"',
      ],
      'defines!': [
        # Regrettably, NSS can't be compiled with NO_NSPR_10_SUPPORT yet.
        'NO_NSPR_10_SUPPORT',
      ],
      'include_dirs': [
        'mozilla/security/nss/lib/base',
        'mozilla/security/nss/lib/certdb',
        'mozilla/security/nss/lib/certhigh',
        'mozilla/security/nss/lib/cryptohi',
        'mozilla/security/nss/lib/dev',
        'mozilla/security/nss/lib/freebl',
        'mozilla/security/nss/lib/freebl/ecl',
        'mozilla/security/nss/lib/freebl/mpi',
        'mozilla/security/nss/lib/nss',
        'mozilla/security/nss/lib/pk11wrap',
        'mozilla/security/nss/lib/pkcs7',
        'mozilla/security/nss/lib/pki',
        'mozilla/security/nss/lib/smime',
        'mozilla/security/nss/lib/softoken',
        'mozilla/security/nss/lib/ssl',
        'mozilla/security/nss/lib/util',
      ],
      'dependencies': [
        'nspr',
        '../sqlite/sqlite.gyp:sqlite',
      ],
      'direct_dependent_settings': {
        'defines': [
          'NO_NSPR_10_SUPPORT',
          'NSS_USE_STATIC_LIBS',
          'USE_UTIL_DIRECTLY',
        ],
        'include_dirs': [
          'mozilla/nsprpub/pr/include',
          'mozilla/nsprpub/lib/ds',
          'mozilla/nsprpub/lib/libc/include',
          'mozilla/security/nss/lib/base',
          'mozilla/security/nss/lib/certdb',
          'mozilla/security/nss/lib/certhigh',
          'mozilla/security/nss/lib/cryptohi',
          'mozilla/security/nss/lib/dev',
          'mozilla/security/nss/lib/freebl',
          'mozilla/security/nss/lib/freebl/ecl',
          'mozilla/security/nss/lib/nss',
          'mozilla/security/nss/lib/pk11wrap',
          'mozilla/security/nss/lib/pkcs7',
          'mozilla/security/nss/lib/pki',
          'mozilla/security/nss/lib/smime',
          'mozilla/security/nss/lib/softoken',
          'mozilla/security/nss/lib/util',
        ],
      },
      'msvs_disabled_warnings': [4018, 4101],
      'conditions': [
        ['target_arch=="ia32"', {
          'sources/': [
            ['exclude', 'amd64'],
          ],
        }],
        ['OS=="mac"', {
          'defines': [
            'XP_UNIX',
            'DARWIN',
            'HAVE_STRERROR',
            'HAVE_BSD_FLOCK',
            'SHLIB_SUFFIX=\"dylib\"',
            'SHLIB_PREFIX=\"lib\"',
            'SOFTOKEN_LIB_NAME=\"libsoftokn3.dylib\"',
          ],
          'sources!': [
            'mozilla/security/nss/lib/freebl/mpi/mpi_x86_asm.c',
          ],
          'xcode_settings': {
            # Can't use 'target_arch=="ia32"' conditional because that is
            # only checked at GYP file generation time.
            'GCC_PREPROCESSOR_DEFINITIONS[arch=i386]': [
              '$(inherited)',
              'NSS_X86_OR_X64',
              'NSS_X86',
              'i386',
            ],
            'GCC_PREPROCESSOR_DEFINITIONS[arch=x86_64]': [
              '$(inherited)',
              'NSS_USE_64',
              'NSS_X86_OR_X64',
              'NSS_X64',
            ],
          },
        }],
        ['OS=="win"', {
          'defines': [
            'XP_PC',
            'WIN32',
            '_WINDOWS',
            'WIN95',
            'SHLIB_SUFFIX=\"dll\"',
            'SHLIB_PREFIX=\"\"',
            'SOFTOKEN_LIB_NAME=\"softokn3.dll\"',
          ],
          'conditions': [
            ['target_arch=="ia32"', {
              'defines': [
                'NSS_X86_OR_X64',
                'NSS_X86',
                '_X86_',
                'MP_ASSEMBLY_MULTIPLY',
                'MP_ASSEMBLY_SQUARE',
                'MP_ASSEMBLY_DIV_2DX1D',
                'MP_USE_UINT_DIGIT',
                'MP_NO_MP_WORD',
              ],
            }],
          ],
        }],
      ],
    },
  ],
}
