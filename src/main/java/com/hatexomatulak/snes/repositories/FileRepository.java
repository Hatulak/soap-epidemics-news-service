package com.hatexomatulak.snes.repositories;

import com.project.xml.types.File;
import lombok.extern.slf4j.Slf4j;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Base64;

@Slf4j
public class FileRepository {

    public File readFile(String path) throws IOException {
        log.info("Loading file  " + path);
        Path filePath = Paths.get(path);
        byte[] bytes = Files.readAllBytes(filePath);
        byte[] encodedFile = Base64.getEncoder()
                .encode(bytes);
        File file = new File();
        file.setName(path);
        file.setFileData(encodedFile);
        return file;
    }

    public String storeFile(String name, byte[] fileData, String folderName) throws IOException {
        String path = "files/" + folderName.replaceAll(" ", "") + "/" + name;
        log.info("Saving file at" + path);
        Path savePath = Paths.get(path);
        byte[] decodedFile = Base64.getDecoder()
                .decode(fileData);
        Files.createDirectories(savePath.getParent());
        Files.write(savePath, decodedFile);
        return savePath.toString();
    }

}

