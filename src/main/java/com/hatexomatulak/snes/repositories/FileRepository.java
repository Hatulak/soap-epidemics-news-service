package com.hatexomatulak.snes.repositories;

import com.project.xml.types.File;
import lombok.extern.slf4j.Slf4j;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

@Slf4j
public class FileRepository {

    public File readFile(String path) throws IOException {
        log.info("Loading file  " + path);
        Path filePath = Paths.get(path);
        byte[] bytes = Files.readAllBytes(filePath);
        File file = new File();
        file.setName(path);
        file.setFileData(bytes);
        return file;
    }

    public void storeFile(String path, File file) throws IOException {
        log.info("Storing file " + path);
        byte[] fileData = file.getFileData();
        Path savePath = Paths.get(path);
        Files.write(savePath, fileData);
    }

}

