package com.hatexomatulak.snes.configs;

import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.web.servlet.ServletRegistrationBean;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.ws.client.WebServiceClientException;
import org.springframework.ws.config.annotation.EnableWs;
import org.springframework.ws.config.annotation.WsConfigurerAdapter;
import org.springframework.ws.context.MessageContext;
import org.springframework.ws.server.EndpointInterceptor;
import org.springframework.ws.transport.http.MessageDispatcherServlet;
import org.springframework.ws.wsdl.wsdl11.DefaultWsdl11Definition;
import org.springframework.xml.xsd.XsdSchemaCollection;
import org.springframework.xml.xsd.commons.CommonsXsdSchemaCollection;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.List;

@Slf4j
@EnableWs
@Configuration
@EnableAsync
public class Config extends WsConfigurerAdapter {
    @Bean
    public ServletRegistrationBean messageDispatcherServlet(ApplicationContext applicationContext) {
        MessageDispatcherServlet servlet = new MessageDispatcherServlet();
        servlet.setApplicationContext(applicationContext);
        servlet.setTransformWsdlLocations(true);
        return new ServletRegistrationBean(servlet, "/service/*");
    }


    @Override
    public void addInterceptors(List<EndpointInterceptor> interceptors) {
        interceptors.add(new EndpointInterceptor() {
            @Override
            public boolean handleRequest(MessageContext messageContext, Object o) throws Exception {
                log.info("[SOAP RESPONSE]");
                try {
                    ByteArrayOutputStream buffer = new ByteArrayOutputStream();
                    messageContext.getResponse().writeTo(buffer);
                    String payload = buffer.toString(java.nio.charset.StandardCharsets.UTF_8.name());
                    log.info(payload);
                } catch (IOException e) {
                    throw new WebServiceClientException("Can not write the SOAP response into the out stream", e) {
                        private static final long serialVersionUID = -7118480620416458069L;
                    };
                }

                return true;
            }

            @Override
            public boolean handleResponse(MessageContext messageContext, Object o) throws Exception {
                log.info("[SOAP REQUEST]");
                try {
                    ByteArrayOutputStream buffer = new ByteArrayOutputStream();
                    messageContext.getRequest().writeTo(buffer);
                    String payload = buffer.toString(java.nio.charset.StandardCharsets.UTF_8.name());
                    log.info(payload);
                } catch (IOException e) {
                    throw new WebServiceClientException("Can not write the SOAP request into the out stream", e) {
                        private static final long serialVersionUID = -7118480620416458069L;
                    };
                }

                return true;
            }

            @Override
            public boolean handleFault(MessageContext messageContext, Object o) throws Exception {

                log.info("[SOAP REQUEST]");
                try {
                    ByteArrayOutputStream buffer = new ByteArrayOutputStream();
                    messageContext.getRequest().writeTo(buffer);
                    String payload = buffer.toString(java.nio.charset.StandardCharsets.UTF_8.name());
                    log.info(payload);
                } catch (IOException e) {
                    throw new WebServiceClientException("Can not write the SOAP request into the out stream", e) {
                        private static final long serialVersionUID = -7118480620416458069L;
                    };
                }

                return true;
            }

            @Override
            public void afterCompletion(MessageContext messageContext, Object o, Exception e) throws Exception {

            }
        });
    }

    @Bean(name = "news")
    public DefaultWsdl11Definition defaultWsdl11Definition1() {
        DefaultWsdl11Definition wsdl11Definition = new DefaultWsdl11Definition();
        wsdl11Definition.setPortTypeName("NewsPort");
        wsdl11Definition.setLocationUri("/service/news");
        wsdl11Definition.setTargetNamespace("http://www.project.com/xml/news");
        wsdl11Definition.setSchemaCollection(newsSchema());
        return wsdl11Definition;
    }

    @Bean(name = "category")
    public DefaultWsdl11Definition defaultWsdl11Definition2() {
        DefaultWsdl11Definition wsdl11Definition = new DefaultWsdl11Definition();
        wsdl11Definition.setPortTypeName("CategoryPort");
        wsdl11Definition.setLocationUri("/service/category");
        wsdl11Definition.setTargetNamespace("http://www.project.com/xml/category");
        wsdl11Definition.setSchemaCollection(schemaCollection());
        return wsdl11Definition;
    }


    @Bean
    public XsdSchemaCollection newsSchema() {
        CommonsXsdSchemaCollection commonsXsdSchemaCollection = new CommonsXsdSchemaCollection(
                new ClassPathResource("types.xsd"),
                new ClassPathResource("news.xsd"));
        commonsXsdSchemaCollection.setInline(true);
        return commonsXsdSchemaCollection;
    }

    @Bean
    public XsdSchemaCollection schemaCollection() {
        CommonsXsdSchemaCollection commonsXsdSchemaCollection = new CommonsXsdSchemaCollection(
                new ClassPathResource("types.xsd"),
                new ClassPathResource("category.xsd"));
        commonsXsdSchemaCollection.setInline(true);
        return commonsXsdSchemaCollection;
    }

}
