from dataclasses import dataclass
from typing import Optional


@dataclass
class _FileParamsBase:
    progress: int
    segment_len: int
    crc32: Optional[bytes]
    metadata_only: bool
    file_size: Optional[int]

    @classmethod
    def empty(cls):
        return cls(
            progress=0, segment_len=0, crc32=None, file_size=None, metadata_only=False
        )

    def reset(self):
        self.progress = 0
        self.segment_len = 0
        self.crc32 = None
        self.file_size = None
        self.metadata_only = False
