import config


class ResumeChunker:

    def chunk_text(self, text: str) -> list[str]:
        """
        Split text into overlapping chunks.
        """

        chunk_size = config.CHUNK_SIZE
        overlap = config.CHUNK_OVERLAP

        chunks = []

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunks.append(text[start:end])

            start += chunk_size - overlap

        return chunks