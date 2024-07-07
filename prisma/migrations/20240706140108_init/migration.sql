-- CreateTable
CREATE TABLE "files" (
    "file_id" TEXT NOT NULL,
    "file_name" TEXT NOT NULL,
    "uploaded_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "files_pkey" PRIMARY KEY ("file_id")
);

-- CreateIndex
CREATE UNIQUE INDEX "files_file_id_key" ON "files"("file_id");

-- CreateIndex
CREATE UNIQUE INDEX "files_file_name_key" ON "files"("file_name");
